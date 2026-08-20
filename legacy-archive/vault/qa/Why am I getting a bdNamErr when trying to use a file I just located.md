---
title: Why am I getting a bdNamErr when trying to use a file I just located?
apple_id: DTS10004124
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2006-11-14'
source_url: https://developer.apple.com/library/archive/qa/qa1392/_index.html
archived_at: '2026-07-18T02:30:30.413719Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1392

# Why am I getting a bdNamErr when trying to use a file I just located?

## Q:  Why am I getting a `bdNamErr` when trying to use a file I just located?

A: Why am I getting a `bdNamErr` when trying to use a file I just located?

A highly probable cause for this situation is that you located the file using BSD APIs such as `opendir` and `readdir`, and you are trying to use the name returned by these APIs with a Core Services File Manager API such as `FSMakeFSRefUnicode` / `FSOpenFork`.

Conversely, if you locate a file using a Core Services File Manager API such as `FSGetCatalogInfoBulk` and try to use it with a BSD API such as `fopen`, it may fail.

While mixing BSD and Core Services File Manager APIs work most of the time, it will fail if the file name contains a forbidden character, and each set of APIs has different rules:

- the BSD APIs allow the colon (":") character but forbid the slash ("/") character in a file name since this character is used as the directory delimiter,
- the Core Services File Manager APIs allow the slash character but forbid the colon character for legacy reasons since it was used as directory delimiter by previous versions of the Mac OS File Manager.

Thus trying to use file names obtained through BSD APIs in Core Services File Manager APIs, or vice versa, can fail at anytime if the file names contain the characters forbidden in the other set of APIs.

To illustrate how both set of APIs react to forbidden characters, you can use Terminal to launch tools which are using BSD APIs and Finder which is using Core Services File Manager APIs.

Use the `touch` command to create the files "Library/test1" and "Library:test2" in your home directory as shown in Listing 1

__Listing 1__  `touch` in Terminal.

```
$ cd ~ $ touch Library/test1 $ touch Library:test2
```

Using the `ls` command, you will see a file named "Library:test2" in your home directory, and a file named "test1" in its Library subdirectory. The BSD APIs interpreted the slash character as a path separator but treated the colon character as a normal character.

Using the Finder to navigate to your home directory, you will see a file named "Library/test2", and a file named "test1" in its Library subdirectory. The colon is replaced by a slash in the first file name to prevent users from seeing and creating file names with colons.

If the code which is mixing BSD APIs and Core Services File Manager APIs is not called in a large iteration but is, for instance, called in response to a user's action on one file, then the preferred solution is to simply use `FSPathMakeRef` and `FSRefMakePath` to convert between the set of APIs.

For performance reasons if the code is called very often, or if you are handling paths of non-existing-yet files (FSRefs cannot be used in that case), an alternate solution is to manually swap colons in slashes when going from BSD to Core Services File Manager and slashes to colons when going from Core Services File Manager to BSD. The names handled by the BSD APIs are UTF-8 C strings. The names handled by the Core Services File Manager APIs are Unicode UniChar arrays. Since you have to use UTF-8 C strings for or from BSD, the simplest solution is to swap the characters in that string.

__Listing 2__  Swapping colons and slashes in a UTF-8 C string.

```
static void SwapColonsAndSlashes(char * str) {     char * cursor = str;     while (*cursor != 0)     {         if (*cursor == ':')         {             *cursor = '/';         }         else if (*cursor == '/')         {             *cursor = ':';         }         cursor += 1;     } }
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-14 | New document that describes the problem caused by different forbidden characters in POSIX and HFS and a solution around the problem. |

