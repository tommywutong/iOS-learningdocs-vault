---
title: The technology behind preview photos
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/08/06/android/the-technology-behind-preview-photos/'
original_language: en
published: 2015-08-06
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c1e2d8a088f7f37d'
translated: false
---

> 原文：[The technology behind preview photos](https://engineering.fb.com/2015/08/06/android/the-technology-behind-preview-photos/)　·　Meta Engineering — iOS

First impressions matter, whether you’re on a first date, in a job interview, or just choosing new decorations for your house. Some of the first things you see when you visit someone’s profile or page on Facebook are the pictures. These pictures are an integral part of the Facebook experience, but sometimes they can be slow to download and display. This is especially true on low-connectivity or mobile networks, which often leave you staring at an empty gray box as you wait for images to download. This is a problem in developing markets such as India, where many people new to Facebook are primarily using 2G networks. Our engineering team took this on as a challenge: What could we design and build that would leave a much better first impression?

![](https://engineering.fb.com/wp-content/uploads/2015/08/GIgHrgBhW2ufXicFAD2CtUgAAAAAbj0JAAAB.jpg)

We initially focused on the cover photo, the beautiful, high-resolution picture at the top of profiles and pages. The cover photo is one of the most visible parts of these surfaces, yet it’s also one of the slowest to load. There were two big reasons for this. First, cover photos often reach 100 KB, even after JPEG compression. That’s a lot of data when you realize that 2G connections might be transferring data as slowly as 32 KB/second. The second reason is subtler. Before downloading a picture, the application makes a network request for the picture’s URL from the GraphQL server. Then, to actually get the image, it uses that URL to make a second network request to the CDN to get the image bytes. The latency of this second network request can be quite long, typically much longer than the first network request. We needed to attack both of these problems simultaneously.

![](https://engineering.fb.com/wp-content/uploads/2015/08/GF4XrgAiGh5P-8wBAJED-kAAAAAAbj0JAAAB.jpg)

## 200 bytes

To address these issues, we asked ourselves if we could create a visual impression of the image using only 200 bytes. Why 200 bytes? In order to remove that second network request, we needed to include some facsimile of the image itself in the initial network request. This in turn meant that the image had to be part of the GraphQL response, but GraphQL isn’t designed to handle full-size image data. It was determined that if we could shrink a cover photo down to 200 bytes, it could efficiently be delivered via the GraphQL response. The cool thing about this solution, if successful, was that it addressed both the small byte requirement and the need for a second network request in one fell swoop.

We estimated that this would allow us to display the preview photo in our very first drawing pass, reducing the total latency to display profiles and page headers significantly. Eventually, we still want to download and display the full-size image from the CDN, but this can be done in the background while ensuring that the user experience still feels snappy and enjoyable. The challenge now became how to squeeze a cover photo into 200 bytes!

![](https://engineering.fb.com/wp-content/uploads/2015/08/GJMHrgDtb11l_LIBAL3BCjgAAAAAbj0JAAAB.jpg)

## Displaying the right image

We felt that a frosted-glass “impression” of an image would provide something both visually interesting and consistent with the original image. Having decided on the desired user experience, we needed to figure out the technical details to make it happen. What was the lowest resolution we could use? How would we compress the image? How would we display that image on the client? This is where things got interesting.

Displaying the image was the most straightforward part: The frosted-glass look is relatively easy to achieve with a Gaussian blur filter. The nice thing about this blurring filter, besides looking good, is that it “band-limits” the signal. Band-limiting essentially means throwing away detail and quickly changing information in the original source image. The more we are willing to blur the displayed image, the smaller our source image can be.

## Image resolution and compression

Clearly, the more we blur our images, the lower resolution we need and the more we can compress. On one extreme, if we send down just the average color of all the pixels in an image (aka the DC components of an image), that would require only a single “pixel” of 3 bytes — one byte each for RGB! We knew we needed higher resolution than just one pixel, but how few pixels could we get away with?

Given the final frosted-glass effect we want to achieve on the client, we can determine the required blur radius for our Gaussian filter. From that blur radius, we were then able to compute the lowest-resolution image that would still give us the desired final image. For the display size of our cover photos, we found that this resolution was about 42 pixels. Above a 42×42-pixel image, we would get no additional fidelity in the displayed image; essentially, we would be wasting data. But assuming 3 bytes per pixel (for RGB components), that would still be 42x42x3, or 5,292 bytes — much higher than the desired 200-byte target.

We started evaluating standard compression techniques to find the best way to compress this data to 200 bytes. Unfortunately, simply entropy encoding the image, with, say, zlib, gets you only a factor of 2. Still too big. We then evaluated a bunch of nonstandard techniques, but we decided it was better to leverage other code/libraries that we had. So, we looked at JPEG image encoding, which is a very popular image codec. Especially since our image is going to be blurred heavily on the client, and thus band-limiting our image data, JPEG should compress this image quite efficiently for our purposes. Unfortunately, the standard JPEG header is hundreds of bytes in size. In fact, the JPEG header alone is several times bigger than our entire 200-byte budget. However, excluding the JPEG header, the encoded data payload itself was approaching our 200 bytes. We just needed to figure out what to do about that pesky header!

![](https://engineering.fb.com/wp-content/uploads/2015/08/GFsHrgAVW5qWY48AABN8FHMAAAAAbj0JAAAB.jpg)

## JPEG to the rescue (mostly)

There are a few tables within the JPEG header, which accounts for its size. The question then became: Would it be possible to generate a fixed header that could be stored on client and therefore not need to be transmitted? In that scenario, only the payload would need to be sent, which would make this the winning format. The investigation began.

For a given Q value, the quantization table is fixed; through experimentation and measurement, Q20 produced an image that would meet our visual needs. So that was a good start to a fixed header. Our images were not a fixed size but capped at 42×42 (we retain the aspect ratio in the reduced format). This amounted to 2 bytes that we could prepend to the payload and that could be placed by the client in the correct spot to make the header valid. As we looked through the rest of the standard JPEG header, the only other table that could change with different images and options was the Huffman table.

This required a bit more work, because there is a trade-off between changes to Q, image data, and image size, which meant different frequency values within the Huffman table, which would lead to different levels of compression and different final payload byte count. Compressing quite a few images while trading off each of those took time, but in the end we had a Huffman table that we could use as a standard that would get us the byte count we wanted across the test images.

Since we deal with a large number of images, it was always possible that the solution wouldn’t scale, there might be extreme edge cases, we didn’t have a real representative sample set, etc. To that end, a version number was added to the beginning so that the format would be future-proof. If we find any extreme cases or better tables in the future, we can update the version number for those images and ship new tables on the clients. So the final format became one byte for version number, one byte each for width and height, and finally the approximately 200 byte payload. The server would just send this format as part of the GraphQL response, and then the client could simply append the JPEG body to the predefined JPEG header, patch the width and height, and treat it as a regular JPEG image. After the standard JPEG decoding, the client could run the predetermined Gaussian blur and scale it to fit the window size. With this, we finally had a format that met our requirements — a highly effective solution that allowed us to reuse the relatively sophisticated JPEG image encoding scheme while transmitting only the data unique to each cover photo.

![](https://engineering.fb.com/wp-content/uploads/2015/08/GIsHrgBNZv-6CsDAOyI01EAAAAAbj0JAAAB.jpg)

In our data, we saw big improvements. For people on a slow connection, this helped speed up profile and page loads by 30 percent. Even on the fastest connections, this ensured that people would always see a cover photo preview immediately, making their overall experience more seamless. It took a lot of creativity to make it happen, but thanks to everyone’s hard work, it paid off!
