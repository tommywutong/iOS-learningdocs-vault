---
title: 'Integrating autoconversion: Facebook’s path from Zawgyi to Unicode'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2019/09/26/android/unicode-font-converter/'
original_language: en
published: 2019-09-27
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:262a2112db850806'
translated: false
---

> 原文：[Integrating autoconversion: Facebook’s path from Zawgyi to Unicode](https://engineering.fb.com/2019/09/26/android/unicode-font-converter/)　·　Meta Engineering — iOS

Myanmar is currently the only country in the world with a significant online presence that hasn’t standardized on [Unicode](https://home.unicode.org/), the international text encoding standard. Instead, Zawgyi is the dominant typeface used to encode Burmese language characters. This lack of a single standard has resulted in technical challenges for many companies that provide mobile apps and services in Myanmar. It makes communication on digital platforms difficult, as content written in Unicode appears garbled to Zawgyi users and vice versa. This is a problem for apps like Facebook and Messenger because posts, messages, and comments written in one encoding are not readable in another. The lack of standardization around Unicode makes automation and proactive detection of violating content harder, it can weaken account security, it makes reporting potentially harmful content on Facebook less efficient, and it means less support for languages in Myanmar beyond Burmese.

Last year, to support Myanmar’s transition to Unicode, we removed Zawgyi as an interface language option for new Facebook users. Next, we worked to ensure that our classifiers for hate speech and other policy-violating content weren’t going to trip over Zawgyi content and began work on integrating font converters to improve the content experience on Unicode devices. Today, to help the country continue its transition to Unicode, we are announcing that we’ve implemented font converters in Facebook and Messenger. Because we know this transition will take time, our Zawgyi-to-Unicode converter will continue to allow people transitioning to Unicode to read posts, messages, and comments even if their friends and family they have not yet transitioned their devices. This post will detail the technical challenges involved in integrating these converters, including how we differentiate Zawgyi text from Unicode, how we can tell whether a device uses Zawgyi or Unicode, and how to convert between the two, as well as some lessons we learned along the way.

![Facebook post without Unicode conversion (left) and with it (right).](https://engineering.fb.com/wp-content/uploads/2019/09/unicode.jpg)

<sub>Facebook post without conversion (left) and with it (right).</sub>

## Why Unicode?

Unicode was designed as a global system to allow everyone in the world to use their own language on their devices. But most devices in Myanmar still use Zawgyi, which is incompatible with Unicode. Which means the people using those devices are now dealing with compatibility issues across platforms, operating systems, and programming languages. In order to better reach their audiences, content producers in Myanmar often post in both Zawgyi and Unicode in a single post, not to mention English or other languages. Zawgyi encoding uses multiple code points for characters and combined renderings; requires twice as many code points to represent only a subset of the script; and vowel code points could appear before or after a consonant (so CAT or CTA reads the same), which leads to search and comparison problems, even within a single document. This makes any kind of communication between systems a huge challenge.

Facebook supports Unicode because it offers support and a consistent standard for every language. In Myanmar, in particular, we support the transition to Unicode because:

- It allows people in Myanmar to use our apps and services in languages other than Burmese. Zawgyi supports entering only Burmese text, while Unicode enables entering minority languages spoken in Myanmar, like Shan and Mon.
- It offers a normalized form for languages in Myanmar, which helps us protect the people who use our apps by detecting policy-violating content and greatly improves the performance of search tools.
- It makes it more efficient for us to review reports of potentially harmful content on Facebook, and content reviewers will be able to review issues without needing to know how the content was encoded.

## A three-pronged approach

When we first started looking at Myanmar encoding, our top priority was making sure our [systems that detect harmful content](https://ai.facebook.com/blog/advances-in-content-understanding-self-supervision-to-protect-people/), such as hate speech, weren’t stumbling over Zawgyi. [We explained our goals for that in this blog post](https://newsroom.fb.com/news/2018/11/myanmar-hria/). The same challenges (such as multiple code points and combined renderings) that make it hard for systems to communicate using Zawgyi also make it hard to train our classifiers and AI systems to effectively detect policy-violating content.

Fortunately, we are not the only company working on this issue, and we were able to use Google’s open source [myanmar-tools](https://github.com/google/myanmar-tools) library to implement our solution. The myanmar-tools library was a major upgrade, in terms of accuracy of detection and conversion, over the regex-based library we had been using. About a year ago, we integrated font detection and conversion to convert all content into Unicode before going through our classifiers. Implementing autoconversion across our products was not a simple task. Each of the requirements for the autoconversion — content encoding detection, device encoding detection, and conversion — had its own challenges.

### Content encoding detection

To perform autoconversion, we first need to know the content encoding, that is, the encoding used when the text was first input. Unfortunately, Zawgyi and Unicode use the same range of code points to represent characters in Burmese and other languages. Because of this, we can’t tell whether a list of code points representing a string should be rendered with Zawgyi or Unicode. Also, not every string of code points makes sense in both encodings. With a model trained on text created in Zawgyi and Unicode, we can assess the probability that a given string was created with a Zawgyi or a Unicode keyboard.

![With a model trained on text created in Zawgyi and Unicode, we can assess the probability that a given string was created with a Zawgyi or a Unicode keyboard.](https://engineering.fb.com/wp-content/uploads/2019/09/Unicode_chart-01.jpg)

Our detection is based on the myanmar-tools library’s approach. We train a machine learning (ML) model on public Facebook content samples for which we already know the content encoding. This model keeps track of how likely a series of code points is to occur in Unicode versus in Zawgyi for each sample. Later, when determining the content encoding of someone’s content, we look at the model’s prediction for whether that sequence of code points was more likely to have been entered in Unicode or in Zawgyi — and we use that result as the content encoding.

### Device encoding detection

Next, we need to know which encoding was used by a person’s phone (i.e., the device encoding) to understand whether we need to perform a font encoding conversion. To do this, we can take advantage of the fact that in one encoding, combining several code points will combine text fragments to create a single character, while in the other encoding those two code points might represent separate characters. If we create a string on-device and check the width of that string, we can tell which font encoding the device is using to render the string. Once we have this information, we can tell the server in future web requests that the device is using Zawgyi or Unicode and make sure any content that is fetched matches. In Myanmar, our client-side logic determines whether the device in question is Zawgyi or Unicode and sends that encoding as part of the locale field in the web request (e.g., my_Qaag_MM).

### Conversion

Next, the server checks whether it is loading Burmese content. If the content encoding and device encoding don’t match, we need to convert the content into a format that the reader’s device will render properly. For instance, if a post was input with a Unicode content encoding, but it’s being read on a Zawgyi encoded device, we convert the text of the post to Zawgyi before rendering it on the Zawgyi device.

It’s important to train this model on Facebook content instead of on other publicly accessible content on the web. People write differently on Facebook than they would on a webpage or in a scholarly paper: Facebook posts and messages are generally shorter and less formal, and they contain abbreviations, slang, and typos. We want our predictions to be as accurate as possible for the content people share and read on our apps.

## Integrating autoconversion at Facebook scale

The next challenge was to integrate this conversion across the different types of content that people can create on our apps. Zawgyi text has been entered for status updates as well as for user names, comments, video subtitles, private messages, and more. Running our detection and conversion every time someone fetches any type of content would be prohibitive in terms of the time and resources required. There’s no single pipeline through which all possible Facebook content passes, which makes it difficult to capture Zawgyi content everywhere someone might enter it. Furthermore, not every web request is made from a person’s device. For example, when notifications and messages are pushed to devices, we can’t run the device encoding logic. Also, messages and comments are often very short, lowering detection accuracy.

The font converter is now fully implemented on Facebook and Messenger. These tools will make a big difference for the millions of people in Myanmar who are using our apps to communicate with friends and family. To continue supporting the people of Myanmar through this transition to Unicode, we are exploring expanding our autoconversion tools to more of the Facebook family of products, as well as improving the quality of our automatic detection and conversion. We also intend to continue contributing to the open source myanmar-tools library to help others build tools to support this transition.
