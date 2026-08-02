---
title: How can I find out what non-RGB pixel formats a codec supports?
apple_id: DTS10002279
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-04-24'
source_url: https://developer.apple.com/library/archive/qa/qa1249/_index.html
archived_at: '2026-07-18T02:30:17.838554Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1249

# How can I find out what non-RGB pixel formats a codec supports?

## Q:  Is there a way for an application to query a codec and find out what non-RGB pixel formats it supports?

A: Codecs supporting non-RGB pixel formats should have a 'cpix' resource included in their public resource list containing the four character codes of their supported non-RGB pixel formats. This information can be retrieved by applications using GetComponentPublicResource.

Listing 1 demonstrates how an application can check to see if a specific non-RGB pixel format is supported by a codec.

__Listing 1__

```
Boolean DoesCodecSupportPixelFormat(Component inComponent,
                                    OSType    inFormat)
{
  Boolean   isSupported = false;
  OSTypePtr *hResource = NULL;
  long      thePixelFormatCount;
  int       i;
  OSErr     err;

  // NOTE: GetComponentPublicResource returns a Handle,
  // not a resource - the caller should dispose this using
  // DisposeHandle

  err = GetComponentPublicResource(inComponent,
                                   'cpix', 1,
                                   (Handle*)&hResource);
  if (err || (NULL == hResource)) goto bail;

  thePixelFormatCount = GetHandleSize((Handle)hResource) / 4;

  for (i = 0; i &lt; thePixelFormatCount && !isSupported; i++)
    isSupported = ((*hResource)[i] == inFormat);

  DisposeHandle((Handle)hResource);

bail:
  return isSupported;
}
```


A codec advertising support for '2vuy', 'r408' and 'v408' would for example, include a 'cpix' resource as part of their public resource list which looks like Listing 2.

__Listing 2__

```
resource 'cpix' (kMyCPIXResID) {
 {
     '2vuy','r408','v408'
 }
};
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-04-24 | Editorial |
| 2004-01-05 | New document that applications can find out if a codec supports non-RGB pixel formats. |

