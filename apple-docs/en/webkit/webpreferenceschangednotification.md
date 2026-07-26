---
title: WebPreferencesChangedNotification
framework: WebKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/webpreferenceschangednotification
source_url: 'https://developer.apple.com/documentation/webkit/webpreferenceschangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webpreferenceschangednotification.json'
content_hash: 'sha256:d9d4b4331e8cfa83'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebPreferencesChangedNotification

<sub>Global Variable</sub>

Posted when the web preference settings are changed.

<sub>macOS</sub>

```objc
extern NSString * WebPreferencesChangedNotification;
```

## Discussion

The notification object is the WebPreferences object that changed. This notification does not contain a `userInfo` dictionary.

## See Also

### WebKit Constants (Legacy)

- [WebActionButtonKey](webactionbuttonkey.md) — An NSNumber object where `0` indicates the left button, `1` indicates the middle button, and `2` indicates the right button. _(deprecated)_
- [WebActionElementKey](webactionelementkey.md) — A dictionary containing element information. See [WebView](webview-swift.class.md) for a description of the key-value pairs in this dictionary. _(deprecated)_
- [WebActionModifierFlagsKey](webactionmodifierflagskey.md) — An unsigned number that indicates the modifier flag. _(deprecated)_
- [WebActionNavigationTypeKey](webactionnavigationtypekey.md) — The navigation type of the action. Can be any of the values defined in [WebNavigationType](webnavigationtype.md) below. _(deprecated)_
- [WebActionOriginalURLKey](webactionoriginalurlkey.md) — The URL that initiated the action. _(deprecated)_
- [WebArchivePboardType](webarchivepboardtype.md) — The pasteboard type constant used when adding or accessing a WebArchive on the pasteboard. _(deprecated)_
- [WebElementDOMNodeKey](webelementdomnodekey.md) — The DOMNode for this element. _(deprecated)_
- [WebElementFrameKey](webelementframekey.md) — The WebFrame object associated with this element. _(deprecated)_
- [WebElementImageAltStringKey](webelementimagealtstringkey.md) — An NSString of the ALT attribute of an image element. _(deprecated)_
- [WebElementImageKey](webelementimagekey.md) — An NSImage representing an image element. _(deprecated)_
- [WebElementImageRectKey](webelementimagerectkey.md) — An NSValue containing an NSRect, the size of an image element. _(deprecated)_
- [WebElementImageURLKey](webelementimageurlkey.md) — An NSURL containing the location of an image element. _(deprecated)_
- [WebElementIsSelectedKey](webelementisselectedkey.md) — An NSNumber used as a BOOL value to indicate whether a text element is selected or not. Zero value indicates false, true otherwise. _(deprecated)_
- [WebElementLinkLabelKey](webelementlinklabelkey.md) — An NSString containing the text within an anchor. _(deprecated)_
- [WebElementLinkTargetFrameKey](webelementlinktargetframekey.md) — The WebFrame object associated with the target of the anchor. _(deprecated)_
