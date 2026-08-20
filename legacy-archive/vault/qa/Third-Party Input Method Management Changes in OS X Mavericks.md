---
title: Third-Party Input Method Management Changes in OS X Mavericks
apple_id: DTS40014100
resource_type: QA
platform: macOS
topic: User Experience
technology: InputMethodKit
published: '2014-01-28'
source_url: https://developer.apple.com/library/archive/qa/qa1810/_index.html
archived_at: '2026-07-18T02:34:53.395299Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1810

# Third-Party Input Method Management Changes in OS X Mavericks

## Q:  Why doesn't my Palette Input Method show up in System Preferences after being copied into the Input Method installation folder in OS X Mavericks?

A: In OS X Mavericks, the Input Sources pane was moved to Keyboard preferences. The pane now only shows keyboard input methods and no longer lists any palette input methods. As a result, if you have installed a palette input method by copying your bundle to ~/Library/Input Methods/ or /Library/Input Methods/ in Mavericks, it would not appear in the Input Sources pane. Additionally, there is no system-provided UI that will allow you to enable or disable it in the Text Input menu of the Apple menu bar.

To make your palette input method visible to users, you must provide your own implementation, such as a preferences pane, to enable your palette after installation. One example is the Character & Keyboard Viewer. You can enable and make it appear in the Text Input menu by selecting a checkbox in the Keyboard pane of Keyboard preferences. See Listing 1 that shows an example on how to enable or disable a palette input method.

__Listing 1__  Enable or disable an input method In the Text Input menu

```objc
- (void)enablePaletteInputMethod:(BOOL)enable {
    const void *key = (const void *)kTISPropertyInputSourceID;
    const void *value = (const void *)CFSTR("<Input Source ID>");
    CFDictionaryRef propertiesDictionary = CFDictionaryCreate(
                                                     kCFAllocatorDefault,
                                                     &key, &value, 1,
                                                     &kCFTypeDictionaryKeyCallBacks,
                                                     &kCFTypeDictionaryValueCallBacks
                                                    );
    if (propertiesDictionary != NULL) {
        CFArrayRef inputSources = TISCreateInputSourceList(propertiesDictionary, TRUE);
        if (inputSources != NULL && CFArrayGetCount(inputSources) > 0) {
            TISInputSourceRef inputSourceRef;
            inputSourceRef = (TISInputSourceRef)CFArrayGetValueAtIndex(inputSources, 0);
            if (inputSourceRef != NULL) {
                if (enable)
                    TISEnableInputSource(inputSourceRef);
                else
                    TISDisableInputSource(inputSourceRef);
            }
            CFRelease(inputSources);
        }
        CFRelease(propertiesDictionary);
    }
}
```

In addition to the above changes, the input modes of keyboard input methods now act like individual input sources in Mavericks. They are no longer grouped under their associated input methods, but are listed in the Input Sources pane.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-01-28 | New document that describes third-party palette and keyboard input method management changes in OS X Mavericks. |

