---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb5.html
archived_at: '2026-07-18T01:25:06.577274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Using%20Your%20Direct%20to%20Web%20Application.md)

## The Login Page

When you launch your application, your web browser displays the Direct to Web login screen:

!

The login page is the default implementation of your Main component, __Main.wo__. It contains text fields to enter a name and password, as well as a submit button (Login) and an Enable Assistant checkbox. To go to the application's default first page, check Enable Assistant and click the Login button. You don't need to enter a name and password, because the default application provides no password-checking logic. If you don't check Enable Assistant before clicking the Login button, you won't have access to the WebAssistant.
You can modify the login page (__Main.wo__) to provide any behavior or appearance you like. For example, you can add your own password-checking logic. See ["Modifying Your Application's Code"](Modifying%20Your%20Application%27s%20Code.md#apple-haytioa)for more information.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb6.md)
