#!/bin/bash

PRIMARY_PROVIDER_NAME="PRIMARY"
SECONDARY_PROVIDER_NAME="SECONDARY"
HOSTS=( 0.0.0.0 ) 
PING_COUNT="4"
MINIMUM_ALIVE_HOSTS="3"
P_IF=""
S_IF=""
P_GW=""
S_GW=""
METRIC="0"
DEFAULT_METRIC="10"


function check_default_route {
  DEFAULT_ROUTE_EXIST=`ip route | grep default | wc -l`
}


function enable_manual_internet_control {
  touch ${MANUAL_INET_CONTROL_FLAG}
}


function disable_manual_internet_control {
  rm -f ${MANUAL_INET_CONTROL_FLAG}
}


function check_manual_control {
  if [ -f ${MANUAL_INET_CONTROL_FLAG} ]; then
      exit 1
  fi
}


function check_internet_state {
  local HOSTS_ALIVE="0"
  for HOST in ${HOSTS[*]}
  do
    ip route add $HOST via $P_GW dev $P_IF metric $METRIC &> /dev/null
    ping -I $P_IF -c${PING_COUNT} ${HOST} > /dev/null 2>&1
    if [ $? -eq "0" ]; then
      ((HOST_ALIVE++))
      HOST_ALIVE_RESULT=${HOST_ALIVE}
    fi
    ip route del $HOST via $P_GW dev $P_IF metric $METRIC &> /dev/null
  done
  if [[ ${HOST_ALIVE_RESULT} -lt ${MINIMUM_ALIVE_HOSTS} ]]; then
    INET_STATE=0
  else
    INET_STATE=1
  fi
}


function activate_primary_provider {
  ip route del default &> /dev/null
  ip route add default via $P_GW dev $P_IF metric $DEFAULT_METRIC &> /dev/null
  ip route flush cache &> /dev/null
  rm -f ${LOCKFILE}
  echo "`date +'%Y/%m/%d %H:%M:%S'` Основной маршрут был изменен на работу с ${PRIMARY_PROVIDER_NAME}" >> ${LOGFILE}
}


function activate_secondary_provider {
  ip route del default &> /dev/null
  ip route add default via ${S_GW} dev ${S_IF} metric $DEFAULT_METRIC &> /dev/null
  ip route flush cache &> /dev/null
  touch ${LOCKFILE}
  echo "`date +'%Y/%m/%d %H:%M:%S'` Основной маршрут был изменен на работу с ${SECONDARY_PROVIDER_NAME}" >> ${LOGFILE}
}


function manual_activate_primary_provider {
  enable_manual_internet_control
  activate_primary_provider
}


function manual_activate_secondary_provider {
  enable_manual_internet_control
  activate_secondary_provider
}


function internet-keepalive {
  check_manual_control
  check_internet_state
  if [ $INET_STATE -eq "1" ] && [ -f ${LOCKFILE} ] ; then
    activate_primary_provider
  fi
  if [ $INET_STATE -eq "0" ] && [ ! -f ${LOCKFILE} ] ; then
    activate_secondary_provider
  fi
  check_default_route
  if [[ ${DEFAULT_ROUTE_EXIST} -eq 0 ]]; then
    activate_primary_provider
    exit 0
  fi
}
if [[ $# -eq 0 ]]; then
  internet-keepalive
