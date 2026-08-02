---
title: How many calls can I make to the Speech Framework API?
apple_id: DTS40017662
resource_type: QA
platform: iOS
topic: User Experience
technology: Speech
published: '2017-07-19'
source_url: https://developer.apple.com/library/archive/qa/qa1951/_index.html
archived_at: '2026-07-18T02:37:35.193619Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1951

# How many calls can I make to the Speech Framework API?

## Q:  What are the rate limits for the Speech Framework APIs?

A: If your application encounters an error similar to the following when using the Speech Framework:

__Listing 1__  Example rate limit error contents.

```
Error Domain=kAFAssistantErrorDomain
Code=203
"SessionId=ffffffff12345678ffffffff12345678ffffffff,
Message=Quota limit reached for resource: speech_api,
actor_type: user,
actor:12345678-ffff-1234-ffff-1234567890ab"
UserInfo={
        NSLocalizedDescription=SessionId=ffffffff12345678ffffffff12345678ffffffff,
        Message=Quota limit reached for resource: speech_api,
        actor_type: user, actor:12345678-ffff-1234-ffff-1234567890ab,
        NSUnderlyingError=0x17404c7b0 {Error Domain=SiriSpeechErrorDomain Code=202 "(null)"}
}
```

Your application is hitting the rate limit defined by the Speech Framework.

The current rate limit for the number of `SFSpeechRecognitionRequest` calls a device can make is 1000 requests per hour. Please note this limit is on the number of requests that a device can make and is not tied to the application making it. This is regardless of the length of audio associated with the request. For a given `SFSpeechRecognitionRequest`, you are allowed up to one minute of audio per request.

Since this is a generous number of requests, if you find yourself hitting the rate limit you should debug your code to better understand why you are making so many requests. If you find you are hitting this limit prematurely you should file a bug report using the [Bug Reporting Tool](https://developer.apple.com/bug-reporting/).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-07-19 | New document that new document that explains the rate limits on calls to the Speech Framework APIs on supported platforms. |

