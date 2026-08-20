---
title: Dynamically registering a bundled component
apple_id: DTS10003334
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2004-06-07'
source_url: https://developer.apple.com/library/archive/qa/qa1083/_index.html
archived_at: '2026-07-18T02:29:55.637793Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1083

# Dynamically registering a bundled component

## Q:  I have a QuickTime Component located in my Application bundle which I would like to register dynamically. Using `CFBundle` APIs, I can find my component bundle, get its resource map then call `RegisterComponentResourceFile`. While this seems to work as expected, calling `OpenAComponent` returns a paramErr. Is there another way to dynamically register a component which resides in an application bundle?

A: You can use the Mac OS X APIs `RegisterComponentFileRef` or `RegisterComponentFileRefEntries`. These APIs allow you to register a file system reference. The Component Manager will correctly register the reference regardless of whether the Component is a Mach-O bundle, standard resource fork based CFM component, CFM bundle, or packaged bundle.

The `RegisterComponentFileRefEntries` API allows you to specify a component description which is used to register selective components.

These APIs are declared in Components.h, part of the CoreServices.framework.

__Listing 1__  Registering a bundled component.

```
OSErr RegisterMyBundledComponent(void)
{
    CFBundleRef mainBundleRef = NULL;
    CFURLRef    resourceURLRef = NULL;
    FSRef       resourceFSRef;
    OSErr       err = paramErr;

    // get the application's main bundle
    mainBundleRef = CFBundleGetMainBundle();

    if (NULL != mainBundleRef) {
        // return the location of a resource
        // contained in the specified bundle
        resourceURLRef = CFBundleCopyResourceURL(mainBundleRef,
                                                 CFSTR("MyBundledComponent"),
                                                 CFSTR("component"), 0);

        if (NULL != resourceURLRef) {
            // convert the url to an FSRef
           if (CFURLGetFSRef(resourceURLRef, &resourceFSRef) == true) {
                // register the component
                // the component manager will "do the right thing"
                // regardless of how the component was built
                // passing false for the second parameter registers the
                // component locally
                err = RegisterComponentFileRef(&resourceFSRef, false);
            }

            CFRelease(resourceURLRef);
        }
    }

    return err;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-06-07 | New document that describes how to dynamically register a Component which resides in an Application bundle. |

