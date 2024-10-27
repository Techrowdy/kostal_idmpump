# kostal_idmpump
using TCP Modbus to send fed-in energy from Kostal Plenticore 10 to iDM AERO SLM 6-17
(iDM Option "TCP Modbus" or "Gebaedeleittechnik/Smartfox" in German Version)

### Defaults
plaese check IPs in kostal_idm.ini file, could be overridden by Docker env variables

### Docker usage

environment variables:

INVERTER_IP (default: 192.168.1.200)

INVERTER_PORT (default: 1502)

IDM_IP (default: 192.168.1.199)

IDM_PORT (default: 502)

FEED_IN_LIMIT (default: 500)

docker run -d --restart always -e INVERTER_IP=192.168.1.5 -e IDM_IP=192.168.1.3 --name kostalidmpump ghcr.io/techrowdy/kostal_idmpump:1.1

### create Docker image for your architecture
./image.sh
