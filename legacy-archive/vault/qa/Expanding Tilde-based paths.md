---
title: Expanding Tilde-based paths
apple_id: DTS10004451
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2008-09-08'
source_url: https://developer.apple.com/library/archive/qa/qa1549/_index.html
archived_at: '2026-07-18T02:32:15.979391Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1549

# Expanding Tilde-based paths

## Q:  How do I expand a tilde-based path to its full path value?

A: How do I expand a tilde-based path to its full path value?

Some situations may arise where you would like to expand a tilde-based relevant path into a resolved, absolute path. For example "~/" might resolve to "/Users/johndoe". Here are examples on how to accomplish this task under each development environment (Objective-C, POSIX and Core Foundation).

__Listing 1__  Objective-C (result is autoreleased)

```
NSString *result = [@"~/Desktop" stringByExpandingTildeInPath];
```


__Listing 2__  POSIX (caller responsible for freeing result)

```c
#include <glob.h>  char* CreatePathByExpandingTildePath(char* path) {     glob_t globbuf;     char **v;     char *expandedPath = NULL, *result = NULL;      assert(path != NULL);      if (glob(path, GLOB_TILDE, NULL, &globbuf) == 0) //success     {         v = globbuf.gl_pathv; //list of matched pathnames         expandedPath = v[0]; //number of matched pathnames, gl_pathc == 1          result = (char*)calloc(1, strlen(expandedPath) + 1); //the extra char is for the null-termination         if(result)             strncpy(result, expandedPath, strlen(expandedPath) + 1); //copy the null-termination as well          globfree(&globbuf);     }      return result; }
```


__Listing 3__  Core Foundation (caller responsible for releasing result)

```c
#include <glob.h>  // This is the POSIX version in listing 2. char*  CreatePathByExpandingTildePath(char* path);  CFStringRef CreateCFStringByExpandingTildePath(CFStringRef path) {     char pcPath[PATH_MAX];     char *pcResult = NULL;     CFStringRef result = NULL;      if (CFStringGetFileSystemRepresentation(path, pcPath, PATH_MAX)) //CFString to CString     {         pcResult = CreatePathByExpandingTildePath(pcPath); //call the POSIX version         if (pcResult)         {             result = CFStringCreateWithCString(NULL, pcResult, kCFStringEncodingUTF8); //CString to CFString             free(pcResult); //free the memory allocated in CreatePathByExpandingTildePath()         }     }      return result; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-08 | Simplified POSIX and CF versions using the embedded glob() function. |
| 2007-09-24 | New document that demonstrates how to resolve tilde-based relevant paths. |

