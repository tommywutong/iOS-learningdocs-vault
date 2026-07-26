---
title: 72 hours to launch Celebrate Pride
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/07/02/android/72-hours-to-launch-celebrate-pride/'
original_language: en
published: 2015-07-02
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:28ec717e5c7c3529'
translated: false
---

> 原文：[72 hours to launch Celebrate Pride](https://engineering.fb.com/2015/07/02/android/72-hours-to-launch-celebrate-pride/)　·　Meta Engineering — iOS

Last Friday, we launched [Celebrate Pride](http://www.facebook.com/celebratepride), a tool that helps people show support for the LGBTQ community by adding a rainbow filter to their profile picture. Over the weekend, more than 26 million people updated their profile picture with the tool, and there were more than 500 million interactions with these photos. The original version of the tool was built by interns solely for Facebook employees. Knowing that the Supreme Court decision on marriage equality was likely coming, we decided to make the tool ready for a global launch, a process we completed in 72 hours. Here’s how we did it.

![](https://engineering.fb.com/wp-content/uploads/2015/07/GHYrrgClKO3vD1ADACMlOGgAAAAAbj0JAAAB.jpg)

It all started during a hackathon, when two interns — Austin Freel and Scott Buckfelder — built the filter as an internal tool for employees. Austin and Scott drew their inspiration from the Pride flags that were draped throughout the Facebook campus in Menlo Park, and they leveraged existing Facebook code to create the rainbow overlay. The tool became popular among employees, and there was great interest in making it available to the public. To do so would require adding a few more people with a few more areas of expertise, like a designer and a PM, to the team.

On Tuesday morning, a small group of us sat down to figure out what it would take to get this out quickly. We wanted to make the tool available in time for the Pride events of the weekend. With the ruling on marriage equality expected later in the week, we had even less time.

![](https://engineering.fb.com/wp-content/uploads/2015/07/GGErrgA2tfaoDC8FAN9NpHUAAAAAbj0JAAAB.jpg)

<sub>Photo by Andrew Valencia Yan</sub>

When we set out, we wanted to make it easy for people to show their support. The interface needed to be simple and the engagement experience instantaneous. The product consists of a single view depicting a preview of the rainbow profile picture, a text field for a caption, and a button to update the photo. This view loads quickly by using CSS layering and deferring the image processing until after the person has decided to use the new photo. The overall network footprint of delivering a preview with markup code is nominal, especially in comparison with downloading an image not distributed across our CDN. By removing all nonessential server processing and stripping away UI chrome, we made it fast and easy for people to update their profile pictures.

We suspected that mobile users would constitute a majority of our traffic. Fortunately, our web stack provides simple abstractions to deliver content optimized for desktop and mobile. Taking advantage of this, we developed an initial concept for desktop and then reused our code for mobile, placing our product in Facebook for iOS, Android, and mobile web in just a few hours. After the launch, the results confirmed our assumptions: Most people were using a mobile device to add the rainbow filter to their profile pictures.

Typically, we would release changes in the afternoon, but to get the product out by Friday morning, we used the Friday 2:00 a.m. code push. This code push was introduced earlier in the month for our London and Tel Aviv engineering offices, and it proved to be a lifesaver for us. Without it, we wouldn’t have been able to launch Celebrate Pride.

Once the product launched, we monitored the performance of the update flow to make sure it was working well for people. From the chart below, we soon realized that there was a high failure rate: The blue line represents the number of attempted updates, while the red line represents the number of successful updates. Upon investigation, we discovered that the failures were caused by large photos (up to 2048 x 2048) being processed by an O(n^2) function. For these photos, it took 4 million loops to process all the pixels, causing the process to time out for some users. During the Friday afternoon code push (a few hours after launch), we shipped a change so that the smaller profile pictures were used instead. Once this fix went live, the number of successful updates increased and the number of failed attempts decreased. In the chart, that’s where the red lines and blue lines converge.

![](https://engineering.fb.com/wp-content/uploads/2015/07/GIgrrgCWUmoozcMBAImBthoAAAAAbj0JAAAB.jpg)

We also used the Friday afternoon code push to make a couple of improvements to the way News Feed stories rendered, which helped accelerate the growth rate of the product. First, we added Open Graph headers to the Celebrate Pride page so that the [https://facebook.com/celebratepride](https://facebook.com/celebratepride) link would be rendered as a visually appealing story attachment when shared.

![](https://engineering.fb.com/wp-content/uploads/2015/07/GLQrrgDzba5cGCcBAE0zWhYAAAAAbj0JAAAB.jpg)

Second, we updated the “changed profile picture” story so that the photo caption would show up inline, making it easier for people to see and share this page with their friends.

![](https://engineering.fb.com/wp-content/uploads/2015/07/GGwGrgB0UicrxOICAEg5lwEAAAAAbj0JAAAB.jpg)

With these two changes, we made it easier for people to share Celebrate Pride with their friends, and we saw a significant increase in the number of people who accessed the tool.

Overall, this project was a great success that touched many lives. We are proud that with the support of a small team, two interns were able to turn a hackathon project into a product used by millions of people within 72 hours.

Acknowledgments: Austin Freel, Scott Buckfelder.
