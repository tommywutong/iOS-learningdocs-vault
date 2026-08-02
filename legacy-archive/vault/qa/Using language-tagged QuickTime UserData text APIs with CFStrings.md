---
title: Using language-tagged QuickTime UserData text APIs with CFStrings
apple_id: DTS40008020
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2005-02-11'
source_url: https://developer.apple.com/library/archive/qa/qa1410/_index.html
archived_at: '2026-07-18T02:30:32.043213Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1410

# Using language-tagged QuickTime UserData text APIs with CFStrings

## Q:  When using `AddUserDataText` I keep getting strange results when adding `UTF-8` text that is intended for a Japanese OS. This API is documented as taking a text string with a language code (`itlRegionTag`), how do I map `UTF-8` strings to the correct language? It would be ideal to just work with `CFStrings`.

A: `AddUserDataText`, `GetUserDataText` and many other QuickTime APIs that take or return text strings assume that the text string is in one of the Traditional Mac OS language specific encodings, for example `kTextEncodingMacJapanese`. Therefore, the value of the `itlRegionTag` parameter passed to these APIs should be the language code, for example `langJapanese`.

If the string you have is `UTF-8` ( or `UTF-16` ), when using `AddUserDataText` you will have to convert it to the appropriate Traditional Mac OS language specific encoding.

`CFString` has the ability to do this conversion by calling `CFStringGetBytes` and passing in the appropriate `CFStringEncoding`.

You can map a Traditional Mac OS language code to the appropriate `TextEncoding` for `CFStringGetBytes` by calling `GetTextEncodingFromScriptInfo` which converts any combination of Traditional Mac OS script code, language code and region code to a `TextEncoding`.

Listing 1 demonstrates how to add a user data text item from a `CFString` using the above technique, while Listing 2 demonstrates retrieving a text user data item as a `CFString`. Because QuickTime requires language-tagged text, you will always need to use the Traditional Mac OS language codes found in `Script.h` with these UserData APIs.

See [Converting Between String Encodings](https://developer.apple.com/documentation/CoreFoundation/Conceptual/CFStrings/Tasks/Converting.html) for more information.

__Listing 1__  Adding a UserData item as text using a language code.

```
/* AddUserDataTextFromCFString  *     Description:         Add a user data item as text to a user data list from a CFString         performing character conversion to a specified language implemented         using a Traditional Mac OS encoding if possible      Parameters:     inUserData - the user data list for this operation     inUDType - the type that is to be assigned to the new item     inIndex - the item to which the text is to be added     inLanguageCode - a language code implemented using a particular Mac OS                      encoding (eg. langEnglish, langJapanese etc.)     inCFString - a CFString containing the user data text to be added      Returns:         noErr or appropriate error code on failure  *  */ OSStatus AddUserDataTextFromCFString(UserData inUserData, SInt32 inUDType, SInt32 inIndex,                                      SInt16 inLanguageCode, CFStringRef inCFString) {     // the string encoding of the characters to copy, the values are the same     // as Text Encoding Converter TextEncoding     CFStringEncoding encoding = 0;     CFIndex numberOfCharsConverted = 0, usedBufferLength = 0;     CFRange range = { 0, CFStringGetLength(inCFString)};     OSStatus status;      // convert any combination of a Mac OS script code, a language code, a region code      // to a text encoding     // the CFString passed in should be in this encoding     status = GetTextEncodingFromScriptInfo(kTextScriptDontCare, inLanguageCode,                                            kTextRegionDontCare, &encoding);     if (noErr == status) {         // grab the characters from a CFString object into a byte buffer after         // converting the characters to a specified encoding         // we initially pass NULL for the destination buffer to make sure the         // conversion will succeed then we check to make sure the entire string can be         // converted as we are not using lossy conversion         numberOfCharsConverted = CFStringGetBytes(inCFString, range, encoding, 0, false,                                                   NULL, 0, &usedBufferLength);         if ((numberOfCharsConverted == CFStringGetLength(inCFString)) && (usedBufferLength > 0)) {             // conversion will work so do it for real this time             Handle hData = NewHandleClear(usedBufferLength);             if (NULL != hData) {                 HLock(hData);                  numberOfCharsConverted = CFStringGetBytes(inCFString, range, encoding, 0,                                                           false, *hData, usedBufferLength,                                                           &usedBufferLength);                 status = AddUserDataText(inUserData, hData, inUDType, inIndex,                                          inLanguageCode);                  DisposeHandle(hData);             } else {                 status = MemError();             }         } else {             // conversion did not work             status = kTextUnsupportedEncodingErr;         }     }      return status; }
```


__Listing 2__  Retrieving language-tagged UserData text as a `CFString`.

```
/* GetUserDataTextAsCFString  *     Description:         Retrieves language code tagged text from an item in a user data list         as a CFString performing character conversion to the appropriate text         encoding if possible      Parameters:     inUserData - the user data list for this operation     inUDType - the type that is to be assigned to the new item     inIndex - the item to which the text is to be added     inLanguageCode - a language code implemented using a particular                      Mac OS encoding (langEnglish, langJapanese etc.)      Returns:         a CFString containing the text or NULL on failure      Note:         it is the responsibility of the caller to release the returned CFString  *  */ CFStringRef GetUserDataTextAsCFString(UserData inUserData, SInt32 inUDType, SInt32 inIndex,                                       SInt16 inLanguageCode) {     TextEncoding encoding = 0; // the encoding of the characters in the buffer     CFStringRef string = NULL;     Handle hData = NULL;     OSStatus status;      hData = NewHandle(0);     if (NULL == hData || noErr != MemError()) return NULL;      status = GetUserDataText(inUserData, hData, inUDType, inIndex, inLanguageCode);     if (noErr == status && (GetHandleSize(hData) > 0)) {         // convert any combination of a Mac OS script code, a language code, a region         // code to a text encoding         status = GetTextEncodingFromScriptInfo(kTextScriptDontCare, inLanguageCode,                                                kTextRegionDontCare, &encoding);         if (noErr == status) {             // create a CFString object from a buffer containing characters in a             // specified encoding             HLock(hData);             string = CFStringCreateWithBytes(kCFAllocatorDefault, (const char *)*hData,                                              GetHandleSize(hData), encoding, false);         }     }      DisposeHandle(hData);      return string; }
```


- [CFStringGetBytes](https://developer.apple.com/documentation/CoreFoundation/Reference/CFStringRef/Reference/function_group_4.html#//apple_ref/doc/uid/20001211/F11133)
- [CFStringCreateWithBytes](https://developer.apple.com/documentation/CoreFoundation/Reference/CFStringRef/Reference/function_group_1.html#//apple_ref/doc/uid/20001211/F11121)
- `GetTextEncodingFromScriptInfo` - This function is almost identical to [UpgradeScriptInfoToTextEncoding](https://developer.apple.com/documentation/Carbon/Reference/Text_Encodin_sion_Manager/tec_refchap/function_group_3.html#//apple_ref/doc/uid/TP30000123/F08036) except it doesn't take a font name and it is available in CoreServices. See `TextCommon.h`
- [AddUserDataText](https://developer.apple.com/documentation/QuickTime/APIREF/adduserdatatext.htm)
- [GetUserDataText](https://developer.apple.com/documentation/QuickTime/APIREF/getuserdatatext.htm)
- [CFStringEncoding](https://developer.apple.com/documentation/CoreFoundation/Reference/CFStringRef/Reference/DataTypeIndex.html#//apple_ref/doc/uid/20001211/C007989)
- [TextEncoding](https://developer.apple.com/documentation/Carbon/Reference/Text_Encodin_sion_Manager/tec_refchap/data_type_21.html)

- Penguins are among the most social of all birds. ("qa1410_UserDataTextUtils.sit", 2.8K)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-02-11 | New document that describes how to use language-tagged QuickTime UserData text APIs with CFStrings and TextEncodings. |

