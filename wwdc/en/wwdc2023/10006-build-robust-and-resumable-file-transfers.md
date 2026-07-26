---
title: Build robust and resumable file transfers
session_id: 10006
collection: wwdc2023
year: 2023
duration: '20:39'
topics: [System Services]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10006/'
content_hash: 'sha256:c3eb5db253e001ec'
translated: false
---

# Build robust and resumable file transfers

<sub>WWDC2023 · 20:39 · System Services</sub>

Find out how URLSession can help your apps transfer large files and recover from network interruptions. Learn how to pause and resume...

> [!note] 归档理由
> 可续传文件传输，涉及 URLSession 后台机制

## Chapters

- [Welcome](/videos/play/wwdc2023/10006/?time=0)
- [Explore the resumable downloads protocol in HTTP](/videos/play/wwdc2023/10006/?time=162)
- [Pause and resume downloads with URLSession](/videos/play/wwdc2023/10006/?time=263)
- [Pause and resume uploads with URLSession](/videos/play/wwdc2023/10006/?time=470)
- [Explore the resumable uploads protocol in HTTP](/videos/play/wwdc2023/10006/?time=585)
- [Add resumable uploads to SwiftNIO](/videos/play/wwdc2023/10006/?time=766)
- [Use background URLSession](/videos/play/wwdc2023/10006/?time=971)

## Resources

- [Welcome](https://developer.apple.com/videos/play/wwdc2023/10006/?time=0)
- [Explore the resumable downloads protocol in HTTP](https://developer.apple.com/videos/play/wwdc2023/10006/?time=162)
- [Pause and resume downloads with URLSession](https://developer.apple.com/videos/play/wwdc2023/10006/?time=263)
- [Pause and resume uploads with URLSession](https://developer.apple.com/videos/play/wwdc2023/10006/?time=470)
- [Explore the resumable uploads protocol in HTTP](https://developer.apple.com/videos/play/wwdc2023/10006/?time=585)
- [Add resumable uploads to SwiftNIO](https://developer.apple.com/videos/play/wwdc2023/10006/?time=766)
- [Use background URLSession](https://developer.apple.com/videos/play/wwdc2023/10006/?time=971)
- [Building a resumable upload server with SwiftNIO](https://developer.apple.com/documentation/Foundation/building-a-resumable-upload-server-with-swiftnio)
- [Downloading files in the background](https://developer.apple.com/documentation/Foundation/downloading-files-in-the-background)
- [URLSession](https://developer.apple.com/documentation/Foundation/URLSession)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10006/4/62804C33-C167-4D42-9E12-390AED4A4EE1/downloads/wwdc2023-10006_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10006/4/62804C33-C167-4D42-9E12-390AED4A4EE1/downloads/wwdc2023-10006_sd.mp4?dl=1)
- [Advances in Networking, Part 1](https://developer.apple.com/videos/play/wwdc2019/712)
- [Pausing and resuming a URLSessionDownloadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=293)
- [Pausing and resuming a URLSessionDownloadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=321)
- [Pausing and resuming a URLSessionDownloadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=371)
- [Retrieving resume data on error](https://developer.apple.com/videos/play/wwdc2023/10006/?time=394)
- [Pausing and resuming a URLSessionUploadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=509)
- [Pausing and resuming a URLSessionUploadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=517)
- [Pausing and resuming a URLSessionUploadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=537)
- [Retrieving resume data on error](https://developer.apple.com/videos/play/wwdc2023/10006/?time=562)
- [Before resumable uploads in Swift NIO](https://developer.apple.com/videos/play/wwdc2023/10006/?time=795)
- [Add resumable uploads in Swift NIO](https://developer.apple.com/videos/play/wwdc2023/10006/?time=846)
- [Informational responses in URLSession](https://developer.apple.com/videos/play/wwdc2023/10006/?time=948)
- [Using background URLSession](https://developer.apple.com/videos/play/wwdc2023/10006/?time=1099)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Jonathan: Hi, I'm Jonathan, and I'm an engineer on the Internet Technologies team. Today we'll explore how to build robust and resumable file transfers using URLSession. Large file transfers can be a huge challenge because even a tiny interruption can throw away all your user's progress and force them to start from the very beginning. Plus, the larger the transfer, the longer it takes, and the longer it takes, the more opportunity there is for something to go wrong.

In that time, your user might navigate away from your app, leave the range of Wi-Fi, or experience one of so many network problems outside of their control. In this session, we'll explore how to solve these challenges and provide a robust networking experience for your users. Our first stop is resumable HTTP protocols, which allow your user to keep their progress when a connection is interrupted. This prevents wasted time and bandwidth, making these protocols a powerful tool when transferring large amounts of data. I'll demonstrate how to resume both downloads and uploads in URLSession, including brand new APIs for resumable upload tasks. Understanding the mechanism behind these APIs can be really helpful for debugging your app, or even building your own server support. That's why we'll also cover the resumable protocols themselves, so you know exactly how your app and server achieve this over HTTP.

Next up, speaking of servers, you'll learn how to bring resumable upload support to any server that uses SwiftNIO.

And lastly, we'll review how background URLSessions can gracefully handle user and network interruptions, while making efficient use of system resources.

Let's learn more about download and upload resumption in URLSession. So I'm downloading the latest Xcode, and the 7 gigabyte download is almost finished. Right at the end, my Wi-Fi goes out.

But wait, the download is paused, and when the Wi-Fi comes back online, I can resume my download from where it left off.

I just saved lots of time and several gigs of bandwidth. Resumable downloads are amazing. But how do they work? First, the client sends a GET request to retrieve the download from the server.

In the response, the server advertises its support for resumable downloads using the Accept-Ranges header. Accept-Ranges: bytes means the server supports range requests for specific bytes of this resource. The server response also contains what's called an ETag, which uniquely identifies the resource at this moment in time. If the content on the server changes, the ETag does, too.

So what happens if this download is interrupted? The client has stored the partial download data, so it only needs the last part. To accomplish this, it can send a range request to retrieve the missing bytes of the download. The request indicates which bytes using the Range field. But the client also needs to make sure the resource hasn't changed, or else it would be appending data from the new resource onto the older resource that's stored. To prevent this, the If-Range field contains the ETag received from the previous response, telling the server to only send the partial data if the ETag is the same.

If the ETag is the same, then the server responds with 206 Partial Content. The Content-Range field here denotes the range of bytes included in this response, completing the download.

Since the beginning, URLSession has offered API to pause and resume download tasks using Range requests. Now, you can pause and resume uploads, too. Not only does this allow you to manually pause an ongoing task, but you can also perform error handling to recover from unexpected connection issues and resume your transfer right where it left off. Let's review how this works for downloads first. Imagine you're creating a UI that allow users to manually pause and resume their downloads. Like the Safari example, your app owns this UI, but under the hood, you can use URLSession to handle all the details, like keeping track of the partial download data, ETag, and request headers. To begin a download, you create a download task like usual, and start it by calling resume. To pause the download, such as when a user taps a pause button, you can call cancelByProducingResumeData. In order to resume this download later, URLSession will need information about the partial download, like its ETag, current size, and location on disk. This, and other metadata, are conveniently stored in the resume data object returned from this function. Again, it's important to note that this resume data is not the partial download data. If the resume data is nil, this means that one or more requirements for resumable downloads are not met, which we'll cover soon. On the other hand, if the resume data is not nil, you should store it for later use. That's because to resume the download, like when a user taps a resume button, you pass this stored data to the downloadTask withResumeData method. It's as simple as that! This pattern is great for manually pausing a download, but URLSession also offers ways to recover from unpredicted connection interruptions.

If your download task fails due to a network problem, you can check for resume data in the error itself. If the download can be resumed, the error's userInfo dictionary will contain that resume data. You can conveniently access this data using the downloadTaskResumeData property of URLError. There are a few requirements for resumable downloads in URLSession. Downloads inherently fetch data, and should be safe to repeat, so URLSession requires the download task to have an HTTP GET request. Other schemes or methods are not supported. Next, the server must support byte-range requests and advertise this using the Accept-Ranges header. The server must provide an ETag, or Last-Modified field, for the resource in the response, but ETag is preferred. And lastly, the temporary download file must not have been deleted by the system in response to disk space pressure.

With these requirements in place, you can manually pause and resume a download, or even recover from connection interruption. Without a resumption protocol, even a small interruption forces you to restart your transfer from the very beginning. This is an even bigger problem for uploads. Upload speeds are often much slower than download speeds, so restarting means even more lost time and resources. iOS 17 introduces brand new support for resumable upload tasks. I'm super excited for these. Now, upload tasks are automatically resumable if the server supports the latest protocol draft. Let's explore the new API first, then dive-in to the details of the resumable upload protocol. Just like download tasks, simply create an upload task and start it by calling resume. To pause, upload tasks now support the same cancelByProducingResumeData method as download tasks. The task automatically detects if the server supports the latest resumable upload protocol. If the server does support it, then you can store the resume data for later use.

And finally, to resume your paused upload, use the new uploadTask withResumeData method. You'll notice the pattern shown here is identical to download tasks. That means if you've already created a great experience for pausing and resuming downloads in your app, you can easily implement resumable uploads for your users, too. If there's just a momentary network interruption, but the server is still reachable, URLSession will automatically try to resume your upload. No extra code is needed. But in case of other, broader connection issues, like if your network or server goes down entirely, you can check the error for resume data, just like download tasks. I'm extremely happy to see resumable uploads in URLSession, and I hope you love them, too. But in order for you to take advantage of this feature, your server must also support the latest resumable upload protocol.

This protocol is currently being developed, and there are efforts across the industry to standardize it in the IETF. In the protocol, the client is able to automatically discover server support. This means URLSession can attempt to make ALL uploads resumable on the very first request. If the server does not support resumable uploads, the request simply continues as a regular upload. Let's see how it works on the wire.

The client first sends a request to an upload endpoint. The Upload-Incomplete field indicates that this client supports resumable uploads. The question mark zero is what's known as a structured field boolean, and it represents the value false. This means that all of the upload data is included in the body of this request.

If the server supports resumable uploads, it detects the client's header and advertises its own support using a 104 informational response. The 104 response contains a location field with a resume URL. This resume URL is used to uniquely identify the upload, so the client knows where to resume the upload if the connection is interrupted. The server associates the upload data it receives with this unique resume URL.

If the upload finishes without interruption, then great. The server sends a 201 and it's done. However, if the upload is interrupted, the client and server perform the resumable upload procedures.

The server has stored the partial upload for the resume URL, but the client needs a way to determine how much data the server actually got. To do this, the client sends a HEAD request to the resume URL, asking the server for the upload offset. This offset is the true number of bytes the server has received.

The server then responds with the upload offset for the client's specific upload.

And lastly, the client needs to acknowledge the server's offset and send the remaining data. To do this, the client sends a PATCH request to the resume URL with a matching upload offset. The body of this request contains the upload data starting from the given offset.

With that, the client has finally sent all the data to the server, completing the upload. Your app gets all this for free using upload tasks in URLSession. Now, let's take a quick trip to the server side and explore how you can build your very own resumable upload server with SwiftNIO.

For those of you already using SwiftNIO on your server, this section is for you. Resumable uploads can be implemented in any server, but if your server already uses SwiftNIO, there's a new package that makes it really easy to add support. Let's go over a quick example. If you're not familiar, SwiftNIO is an asynchronous network application framework that works in your app and server. In this sample code, we're setting up an HTTP/2, server. We've added two handlers to our server. The codec translates HTTP/2 frames into requests our example handler can understand. In the other direction, it takes responses from the example handler and codes them into HTTP/2 frames. The ExampleChannelHandler performs the basic routing and logic for our server. At first, we only support regular uploads. Let's find out how easy it is to transform our server to support resumable uploads.

First, we download the NIOResumableUpload project, add it as a dependency, and import it in our code. Then, we define a resumable upload context. This tells the handler which upload endpoint to use when generating resume URLs.

And lastly, we wrap our current handler in the HTTPResumableUploadHandler. This performs the resumable upload procedures on top of our current logic. For each upload, it generates a random and secure resume URL and associates this with the upload data. If a connection is interrupted, the handler holds on to any partial data and responds to all the resumable upload procedures for us. Wow! With just a few lines of code, we've supercharged our server to support resumable uploads. For those of you using Swift on Server already, try this out! And for everybody regardless, be sure to check out the open-source sample code from the link in the description. The sample code also uses new HTTP types, which allow you to use the same types across your app and your Swift on Server projects. These data types were released as an open-source package in collaboration with SwiftNIO, so check out the Swift blog to learn more and provide your feedback.

You might have noticed the resumable upload protocol makes use of informational responses using the 104 status code. The new HTTP Types make it easy to support these responses on the server side. In your app, URLSession handles the 104 response automatically for resumable uploads. But on top of that, URLSession now provides a delegate method didReceiveInformationalResponse. This allows your app to handle other intermediate responses such as 102 Processing or 103 Early Hints.

Resumable protocols are a great way to alleviate network interruptions and save bandwidth. Background URLSession can also be useful when handling large file transfers. Imagine your user wants to upload a huge 4K video from their latest ski trip. If their connection gets interrupted, you want to make sure to resume the upload if possible. You could do all the error handling yourself. Or, you can let background session do it for you.

In fact, background session will handle resumption automatically for both download and upload tasks, if the server supports it.

If a task is interrupted, the system will try to resume the task at increasing time intervals.

If the task cannot be resumed, the system will automatically retry the task from the beginning.

Maybe your user loses cell coverage on the ski mountain, or a snowstorm took out their Wi-Fi. Background session always waits for connectivity, so tasks will be scheduled at some point after the device connects to the internet again.

While your user is uploading their video, they might leave your app or put their device away. Maybe they're getting ready to shred more some powder, and they still expect their upload to continue.

This specifically calls for a background session. Background tasks are scheduled by the system, so they run outside your app's process. This means even if your app is suspended or terminated by the system, your network tasks continue reliably. Use a background session for large file transfers that might take a long time and need to persist when a user leaves your app.

Lastly, your user deserves the best experience when they're in your app, and that might mean scheduling less urgent tasks to happen at a later time. By using a background session, you have several ways to efficiently schedule network activity and save resources for your user.

For tasks that don't need to happen immediately, consider setting the isDiscretionary property to true on your background configuration. This allows the system to intelligently schedule your tasks, taking into account factors like "Is the user on Wi-Fi", "is their device connected to power", and "is the network constrained"? This can be a great option when downloading assets for later use, or uploading a nightly backup, or analytics.

To prevent using too much bandwidth on Low Data Mode, consider setting the allowsConstrainedNetworkAccess property to false. Check out the Advances in Networking session for more tips on supporting Low Data Mode in your app.

You can also schedule the background task itself to begin at a later time, when a person is less likely to be using system resources. Late at night is often a great time for scheduling tasks like large backups.

To further assist the system scheduling, we can set the countOfBytesClientExpectsToSend and Receive properties. By utilizing these properties, you're empowering the system to best allocate resources and passing those benefits on to your users. Background session is a great tool for large file transfers that don't need to happen immediately or transfers that should continue when your app is suspended. For smaller tasks, or tasks that need to happen as soon as possible, you can use a standard URLSession. Make networking reliable for your users by bringing the power of resumption to your app. Check out SwiftNIO and HTTP Types, and let's work together to create the best HTTP experience in Swift. And lastly, try using background session for large or discretionary file transfers. You'll find lots of ways to save resources for when your user needs it most. Thanks for watching, and be sure to check out these other great networking sessions below. And that's a wrap! ♪ ♪
