---
title: Sherlock Channels
apple_id: 10000121i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-04-09'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Sherlock/Tasks/CreatingWebServices.html
archived_at: '2026-07-15T05:18:57.646302Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sherlock Channels](Introduction%20to%20Sherlock%20Channels.md)


[Next](Trigger%20Examples.md)[Previous](Printing%20Your%20Channel%E2%80%99s%20Content.md)

# Using Web Services

The following tasks show you how to create and use web services in your channel. Web services are remote functions that clients call over an intranet or the Internet to perform specific tasks. For example, the publisher of a stock website can define a service that takes a stock symbol and returns the current price of that stock. Sherlock also defines a type of web service that you link to from your channel code to take advantage of its functionality. You can use existing web services or you can define your own web services to separate out code from your channel that you want to share.

To publish a new web service, you must first assemble the code file containing your web service code. You place your web service code in an XML file. Because web services contain script code, you use the `<scripts>` tag as the top-level element wrapping your code. When declaring web services, you do not need to include any attributes for this tag. However, when you want to load a web service, you should include a `src` attribute to specify the location of the web service code file.

Inside the `<scripts>` tag, put a `<script>` tag and include the language attribute identifying the type for your functions. The content of the `<script>` tag is the functions you want to define. You can include multiple script tags if your service includes both JavaScript and XQuery syntax.

The following listing illustrates one way to write a web service for finding city, state, and zip code information. The service defines two functions using the XQuery language.

```
<!-- Copyright (c) 2002, Apple Computer, Inc. -->
<!-- All rights reserved.                     -->

<scripts>
<script language="XQuery">

{-- CityStateZipFromZip -  return city/state/zip --}
define function CityStateZipFromZip($zip)
{
    let $query_url := "http://www.usps.gov/cgi-bin/zip4/ctystzip2"
    let $post_data := concat("ctystzip=", $zip)/url-encode(., " ", "+")/
                translate(., " ", "+")
    let $start := "----------&lt;BR&gt;"
    let $end := "ACCEPTABLE"
    let $computedCityAndState := http-post($query_url, $post_data)/DATA/
                data-match(., $start, $end)/normalize-space()
    let $computedCityAndStateArray := string-separate($computedCityAndState,
                " ")
    let $computedState := item-at($computedCityAndStateArray,
                count($computedCityAndStateArray))
    let $computedCity := substring-before($computedCityAndState,
                $computedState)/normalize-space()
    let $newCity := if ($computedCity) then $computedCity else $city
    let $newState := if ($computedState) then $computedState else $state
    return dictionary(
        ("city", $newCity),
        ("state", $newState),
        ("zip", $zip))
}

{-- CityStateZipFromCityState --}
define function CityStateZipFromCityState($city, $state)
{
    let $query_url := "http://www.usps.gov/cgi-bin/zip4/ctystzip2"
    let $post_data := concat("ctystzip=", $city, " ", $state)/
                url-encode(., " ", "+")/translate(., " ", "+")
    let $computedZip :=  http-post($query_url, $post_data)/DATA/
                data-match(., "&lt;BR&gt;&lt;BR&gt;", "ACCEPTABLE")/
                normalize-space()
    let $firstComputedZip := string-separate($computedZip, " ")[1]
    let $newZip := if ($firstComputedZip) then $firstComputedZip else $zip
    return dictionary(
        ("city", $city),
        ("state", $state),
        ("zip", $newZip))
}
</script>
</scripts>
```

Making your services available is a simple process of placing your web service code file on your web server and notifying clients where they can find it. If you are going to make your web services available to the public, you should also document the syntax for your functions. Clients can then include the code in their scripts using the `<scripts>` tag.

In addition to defining your own services, you can also use Sherlock to access other web services using the Simple Object Access Protocol (SOAP). To generate a SOAP request, you must construct the XML query required by the target server. You can then send the request using the Apple-provided functions `http-post` and `http-request`.

The following example, written in XQuery, shows you how to access a SOAP web service for retrieving stock prices. In this example, the `StockSymbolLookup` function creates the XML objects to be passed to the SOAP server as part of the request. The data is then passed to the SOAPQuery method, which creates a set of default HTTP headers, posts the request, and returns the result.

```
{-- SOAPQuery: executes the query --}
define function SOAPQuery($query, $action, $soapAddress)
{
    {-- set the content type and the soap action for the request --}
    let $headers := dictionary (
            ("Content-Type", "text/xml; charset=utf-8"),
            ("SOAPAction", $action)
        )

    {-- send the request --}
    return http-post($soapAddress, $query, $headers)/DATA
}

{-- StockSymbolLookup based on --}
{-- http://services.xmethods.net/soap/urn:xmethods-delayed-quotes.wsdl --}
define function StockSymbolLookup($symbol)
{
    {-- construct the XML query --}
    let $soapQuery :=
    <SOAP-ENV:Envelope
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/1999/XMLSchema">
        <SOAP-ENV:Body>
            <ns1:getQuote
                xmlns:ns1="urn:xmethods-delayed-quotes"
                SOAP-ENV:encodingStyle=
                    "http://schemas.xmlsoap.org/soap/encoding/" >
                <symbol xsi:type="xsd:string" > { $symbol } </symbol>
            </ns1:getQuote>
        </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>

    {-- send the request and parse out the result --}
    return SOAPQuery($soapQuery, "urn:xmethods-delayed-quotes#getQuote",
            "http://66.28.98.121:9090/soap")//Result/number()
}
```

To retrieve a stock quote, you would then call the `StockSymbolLookup` function from your code, as shown in the following example:

```
let $stockValue := StockSymbolLookup("AAPL")
```

[Next](Trigger%20Examples.md)[Previous](Printing%20Your%20Channel%E2%80%99s%20Content.md)

