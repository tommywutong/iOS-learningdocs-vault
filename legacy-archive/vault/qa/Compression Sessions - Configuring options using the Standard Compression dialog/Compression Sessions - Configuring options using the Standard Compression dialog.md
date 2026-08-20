---
title: Compression Sessions - Configuring options using the Standard Compression dialog
apple_id: DTS10003829
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-01-12'
source_url: https://developer.apple.com/library/archive/qa/qa1456/_index.html
archived_at: '2026-07-18T02:30:49.372172Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1456

# Compression Sessions - Configuring options using the Standard Compression dialog

## Q:  Is there an easier way to configure Compression Session options or does each option have to be set by hand?

A: Yes there is an easier way by using the UI provided by Standard Compression.

The Standard compression dialog component provides applications with a high level consistent user interface for specifying the parameters that control compression operations, and allows for easy configuration of a Compression Session options object. Figure 1 shows what this dialog looks like when configuring the H.264 codec.

__Figure 1__  Standard Compression dialog.

!

Listing 1 demonstrates one way to use the Standard Compression component to retrieve Compression Session options.

Once the Standard Compression dialog has been dismissed, call `SCCopyCompressionSessionOptions` to retrieve the fully configured `ICMCompressionSessionOptionsRef` which can be passed to `ICMCompressionSessionCreate`.

The newly created Compression Session will retain this options object. Call `ICMCompressionSessionOptionsRelease` once the Compression Session is created if your application will not be modifying any compression options during the compression operation.

__Listing 1__  Using Standard Compression to configure Compression Session options.

```
ICMCompressionSessionOptionsRef GrabCSessionOptionsFromStdCompression()
{
    ComponentInstance stdCompression = 0;
    long scPreferences;
    ICMCompressionSessionOptionsRef sessionOptionsRef = NULL;

    ComponentResult err;

    // open the standard compression component
    err = OpenADefaultComponent(StandardCompressionType, StandardCompressionSubType, &stdCompression);
    if (err || 0 == stdCompression) goto bail;

    // Indicates the client is ready to use the ICM compression session API to perform compression operations
    // StdCompression will disable frame reordering and multi pass encoding if this flag not set because the
    // older sequence APIs do not support these capabilities
    scPreferences = scAllowEncodingWithCompressionSession;

    // set the preferences we want
    err = SCSetInfo(stdCompression, scPreferenceFlagsType, &scPreferences);
    if (err) goto bail;

    // display the standard compression dialog box
    err = SCRequestSequenceSettings(stdCompression);
    if (err) goto bail;

    // creates a compression session options object based on configured settings
    err = SCCopyCompressionSessionOptions(stdCompression, &sessionOptionsRef);

bail:
    if (0 != stdCompression) CloseComponent(stdCompression);

    return sessionOptionsRef;
}
```


[Image Compression Dialog Component](https://developer.apple.com/documentation/quicktime/RM/CompressDecompress/ImageComprDialog/index.html?http://developer.apple.com/documentation/quicktime/RM/CompressDecompress/ImageComprDialog/rmImageCompDialog/chapter_1_section_2.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-01-12 | New document that discusses how to configure Compression Session options using Standard Compression dialog. |

