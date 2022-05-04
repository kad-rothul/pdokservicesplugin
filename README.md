## PDOK Service Plugin

## English

This plugin is probably only interesting for the dutch audience.

It shows a list of available web services (WMS, WMTS, WFS etc) from our
national data services (in our national crs epsg:28992).
Further information in dutch below.

If you think this plugin is usefull, consider to donate via Paypal button below, OR sent me a kind email of tweet :-)

## Nederlands

PDOK (Publieke Data Op de Kaart) is een eenvoudige plugin om de verschillende
PDOK services te testen of te bekijken.

Op basis van een json bestand (IN de plugin) met alle op dit moment beschikbare
services wordt een dialoog opgebouwd met daarin

- het soort service (WMS, WMTS, WFS of TMS)
- de naam van de service
- een regel per laag van de service

Door op een item te klikken wordt de service direkt aangeroepen een getoond.

Alle services zijn epsg:28992

Als je deze plugin handig vind, laat me dan weten via een vriendelijk briefje of email,
betaal een biertje ( of heel avondje ;-) ) via een [Tikkie](https://tikkie.me/pay/45aaobhg297k0uncn0ms) of een [ASN Betaalverzoek](https://diensten.asnbank.nl/online/betaalverzoek/#/9091261-SuCci9eSvW0qSIBOVUyhJ5APf4AeaW45)
OF doe een donatie via de Paypal button, dan koop ik daar een biertje voor tijdens een reisje naar een QGIS hackfest ofzo...

[![paypal](https://www.paypalobjects.com/en_US/NL/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=DZ8R5JPAW55CJ&currency_code=EUR&source=url)


## Developers

Install dev tools with:

```sh
pip3 install -r pdokservicesplugin/requirements/dev.txt
```

Lint python code with:

```sh
pylint --errors-only --disable=E0611 pdokservicesplugin
```

Format python code with:


```sh
black pdokservicesplugin
```