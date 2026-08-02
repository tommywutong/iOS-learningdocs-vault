---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb25.html
archived_at: '2026-07-18T01:24:57.333492Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb24.md)

## Linking to a Direct to Web Page

In addition to embedding static Direct to Web components, your application can link directly to a dynamically-generated page of the appropriate type. The technique for doing this has two basic requirements:

- A page-wrapper component for the dynamically-generated page
- An action method that returns a Direct to Web component implementing the appropriate page interface

For pages whose next page is dynamically determined (such as query pages), the action method must do more than simply return the page component. See ["Setting Up a Next-Page Callback"](DirectToWeb27.md#apple-gezdsmzu) for detals.

### Setting Up the Page Wrapper

Every application that links to a dynamically-created Direct to Web page must have a component called __PageWrapper.wo__. This component acts as a "wrapper" for the dynamically-generated content, and can have customized header and footer material. The following example shows how to set up the __PageWrapper.wo__ component. You can use a text editor, Project Builder, or (preferably) WebObjects Builder to construct this component.
__PageWrapper.html__ example:

```
<html>
<webObject name=Head></webObject>
<webObject name=BodyContainer>
<webObject name=Body></webObject>
</webObject>
 </html>
```


__PageWrapper.wod__ example:

```
BodyContainer: WOBody {
    filename = "Images/bkg.jpg";
    framework = "DodgeDemo";
        bgcolor="#c0c0c0";
    TEXT = "#000000";
    LINK = "#0000F0";
    VLINK = "#0000F0";
    ALINK = "#FF0000";
}

Head : D2WHead {
    _unroll = YES;
}

Body: WOComponentContent {
    _unroll = YES;
};
```


The only required component in __PageWrapper.wo__ is the WOComponentContent. The other components shown in the example are optional, and you can create your own header, footer, and body-container components for your dynamically-generated pages.
The ___unroll__ attribute, when YES, enables the WebAssistant to generate a static component from the dynamically-generated one.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb26.md)
