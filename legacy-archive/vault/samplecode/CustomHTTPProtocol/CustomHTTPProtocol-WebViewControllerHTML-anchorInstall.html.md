---
title: CustomHTTPProtocol
apple_id: DTS40013653
resource_type: Sample Code
platform: iOS
topic: null
technology: Foundation
published: '2014-08-20'
source_url: https://developer.apple.com/library/archive/samplecode/CustomHTTPProtocol/Listings/CustomHTTPProtocol_WebViewControllerHTML_anchorInstall_html.html
archived_at: '2026-07-18T03:05:34.858909Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CustomHTTPProtocol](CustomHTTPProtocol.md)


[Next](CustomHTTPProtocol-WebViewControllerHTML-error.html.md)[Previous](CustomHTTPProtocol-WebViewController.m.md)

# CustomHTTPProtocol/WebViewControllerHTML/anchorInstall.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>Anchor Install</title>
    <script type="text/javascript">

function didStartInstall()
{
    var e

    e = document.getElementById("installSpinner")
    e.style.display = "inline"

    e = document.getElementById("installText")
    e.innerText = "Installing..."

    e = document.getElementById("installButton")
    e.parentNode.removeChild(e)
}

function didFinishInstall()
{
    var e

    e = document.getElementById("installSpinner")
    e.style.display = "none"

    e = document.getElementById("installText")
    e.innerText = "Installed!"
}

    </script>
</head>
<body>
<h1>Anchor Install</h1>
<p>
URL: %@
</p>
<form name="input" action="%@" method="put">
<img id="installSpinner" src="spinner.gif" alt="Install Spinner" style="display:none" />
<span id="installText"></span>
<input id="installButton" type="submit" value="Install" />
</form>
</body>
</html>
```

[Next](CustomHTTPProtocol-WebViewControllerHTML-error.html.md)[Previous](CustomHTTPProtocol-WebViewController.m.md)

