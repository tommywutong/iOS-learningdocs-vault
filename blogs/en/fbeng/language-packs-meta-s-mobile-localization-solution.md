---
title: 'Language packs: Meta’s mobile localization solution'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2022/05/09/android/language-packs/'
original_language: en
published: 2022-05-09
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1e479bd7f85007bc'
translated: false
---

> 原文：[Language packs: Meta’s mobile localization solution](https://engineering.fb.com/2022/05/09/android/language-packs/)　·　Meta Engineering — iOS

More than 3 billion people around the world rely on our services each month. On mobile, around 57 percent of people on Facebook for Android and 49 percent of those on Facebook for iOS use the app in a language other than English. Delivering the best experience for these people, in their own language, is an important step in helping people around the world connect. That means providing people with an interface in their local language, and making sure it is accurate — down to the grammar, gendered nouns, plurals, etc. With dozens of languages (more than 100 for some interfaces) to accommodate in every UI interface across our app, that’s a big challenge. To solve for this, we’ve developed a custom mobile localization infrastructure, which includes downloadable language packs — a download-on-demand translation delivery solution for Android and iOS. Language packs enable us to provide a high-quality user experience that’s localized for people around the world. With this infrastructure, engineers have the ability to create and deliver gendered translations in a simple and intuitive way. This infrastructure has already been adopted by Facebook and Workplace, and we are exploring integrating it into our other Meta apps. With language packs, we have reduced the IPA size of Facebook for iOS by 16.6 MB, which helps it stay fast and responsive for the people who use it.

## Why do we need language packs?

The traditional localization frameworks offered by native Android and iOS platforms present two key scaling issues.

### Issue 1: Accuracy of translation

Native Android and iOS localization frameworks only support simple plain text and pluralized text, making it difficult to create gendered text without boilerplate code. To provide billions of people around the world with a quality localized experience, we have developed our own string API and framework — ours is called [**FBT**](https://facebook.github.io/fbt/). FBT supports PHP, Hack, Javascript, and React Native. This API allows us to define and ship grammatically correct translated texts, including both viewer and subject gendered text, in a simple and intuitive way.

FBT API

```javascript
fbt(
   'Write on ' +
     fbt.pronoun('possessive', gender) +
     ' timeline...',
   'Placeholder text for inline composer',
 )
```

Android

```javascript
 <string name="title_male" description="Placeholder text for inline composer">Write on his timeline...</string>
 <string name="title_female" description="Placeholder text for inline composer">Write on her timeline...</string>
 <string name="title_other" description="Placeholder text for inline composer">Write on their timeline...</string>
```

IOS

```javascript
if (gender == Male) {
  FBLocalizedString("Write on his timeline...", "Placeholder text for inline composer");
} else if (gender == Female) {
  FBLocalizedString("Write on her timeline...", "Placeholder text for inline composer");
} else {
  FBLocalizedString("Write on their timeline...", "Placeholder text for inline composer");
}
```

### Issue 2: Language support and app size

All native mobile strings and react native strings should be translated into the proper formats and built in the app bundle before submitting to the app store. But, as we support more languages and features in the app, its size increases quickly. People can be reluctant to upgrade to newer versions of the app due to bandwidth and device storage challenges. Consequently, new features and improvements would not then be delivered to people’s devices and would prevent them from getting important security updates.

When Facebook for iPhone supported 35 different language locales for people all over the world, we did an app size test for the Facebook iOS app and realized that by removing all the translation files from the bundle, we could save up to 16.6 MB in download size. Since most people use only one language on their device, the rest of translation files in the bundle would be a wasted resource, anyway, taking up space unnecessarily.

Considering these issues, we expanded on a solution called downloadable language packs, initially developed on Android. To support the FBT API and to ship accurate translations on mobile, each language pack file includes all translation variations. To simultaneously support more languages and limit app size, we provide a download-on-demand solution for language packs, where devices download only the language pack file to be utilized. Since enabling downloadable language packs, we have added nearly a dozen more languages, including Burmese, Georgian, Latvian, and Sinhala to Facebook on Android without any impact to app size.

## End-to-end flow

There are two big stages to the language packs framework: One stage occurs before the mobile build release, and the other occurs after it. While we build app binaries, we also construct language packs for the FBT strings used in the build. To adopt new strings and recent updates for translations, each release build must be associated with its language pack in our cloud storage before submitting to the app store. When the release build is published in the app store, the language pack is downloaded from cloud storage or loaded from a disk during localization initialization as part of app startup. The client side will access the language pack file and load the translation data into memory. Later, whenever the string API is called, we look up its translation from parsed data.

![There are two big stages to the language packs framework: One stage occurs before the mobile build release, and the other occurs after it.](https://engineering.fb.com/wp-content/uploads/2022/05/LangPack_1.jpg)

## Constructing language packs

Every day, a number of native strings are created or modified in the codebase for each Meta app. We built an automated pipeline to extract strings, collect translations from the database, and bundle them. For every released mobile build, we have a build step to construct language packs for all supported locales based on the strings in the latest release version and upload the language packs to our cloud storage.

![For every released mobile build, we have a build step to construct language packs for all supported locales based on the strings in the latest release version and upload the language packs to our cloud storage.](https://engineering.fb.com/wp-content/uploads/2022/05/LangPack_2.jpg)

## FBT string creation

FBT is an open source localization framework that provides a more efficient way of defining content for flexible and high-quality localization. This is a simple function wrapper of what would otherwise be English text. The framework is designed to be easy for engineers to use.

Example: simple text

```javascript
fbt('Hello, World', 'a simple example', {project:"foo"})

// Translation: "Hello, World"
```

Example: complex string

```javascript
fbt("View " +
     fbt.name('user', shortName, gender) +
       "'s Timeline - " +
       fbt.plural('follower', count, {many: 'followers', showCount: 'yes'}),
     'In user composer, gives details about the person to who the post is directed.',
   )

// Translation: "View Lu's timeline - 1 follower"
// Translation: "View Lu's timeline - 5 follower"
```

### Extraction

Our pipeline collects **`fbt()`** from codebase and transforms it into the abstract extracted object. In the extracted object, two types of information will be used to construct language packs

- **`id`** — hashed key determined by text + description + relevant metadata
- **`text_or_table`** — A multilevel lookup table, with lookup values defined at each level based on the FBT `callsite`

Example: extracted object of complex string in above section

```javascript
[
  {
     "description":"In user composer, gives details about the person to who the post is directed.",
     "id":"4sIjkwerw",
     "text_or_table":{
        "UNKNOWN":{
           "ONE":"View {user}'s Timeline - 1 follower",
           "OTHER":"View {user}'s Timeline - {number} followers"
        }
     },
            "variations": [
                {
                    "type": "GENDER",
                    "token": "user"
                },
                {
                    "type": "NUMBER",
                    "token": "number"
                }
            ],
            "tokens": {
                "name": "%1$@"
                "number": "%2$ld"
            }

  },
]
```

## Language pack structure

Once we collect all extracted objects, the language packs’ build step will fetch translations from the database and encode them in a binary format. The high-level structure for each language pack file is a hash map table.

```
Language_pack

|

|____ resource_id_1 : nested_fbt_resource_data

|

|____ resource_id_2 : nested_fbt_resource_data

|

|...
```

- **`resource_id`** — same as “id” in the extracted object. This unique key will be used by the client side to find translations at runtime.
- **`nested_fbt_resource_data`** — a multi-level lookup table, with lookup values defined at each level based on the FBT token

- Each token has a type and possible variations (e.g., gender, plural)
- Number of levels and lookup values determined by the FBT API `callsite`
- FBT token values are known only at runtime, so dictionary lookup happens at runtime

Example: `nested_fbt_resource_data` of complex string in Greek’s language pack

```javascript
{
   "4sIjkwerw":{
      "male":{
         "one":"Δείτε το Χρονολόγιο του {user} - 1 ακόλουθος",
         "other":"Δείτε το Χρονολόγιο του {user} - {number} ακόλουθοι"
      },
      "female":{
         "one":"Δείτε το Χρονολόγιο της {user} - 1 ακόλουθος",
         "other":"Δείτε το Χρονολόγιο της {user} - {number} ακόλουθοι"
      },
      "default":{
         "one":"Δείτε το Χρονολόγιο του χρήστη {user} - 1 ακόλουθος",
         "other":"Δείτε το Χρονολόγιο του χρήστη {user} - {number} ακόλουθοι"
      }
   }
}
```

## Using language packs in app

Once the client side adopts the downloadable language packs infrastructure, translations are loaded from the language pack binary file downloaded in an on-demand fashion rather than as a bundled string resource file. In order to deliver translations to all UI views, the localization initialization step has to be completed before rendering the first UI view. After network setup is finished, localization setup can be kicked off immediately. Localization setup is an asynchronous step in startup. In this step, we will check whether the language pack file for a specific locale and client version is on disk. If this file exists, it will be decompressed, parsed, and loaded into memory. However, if this file cannot be found in storage, we will kick off a network request to download the corresponding language pack binary file. If the localization setup is finished before rendering the first UI view, the user experience will be seamless. On the contrary, if the download request is still being processed or the file could not be processed correctly, users have to retry the download or fall back to the previous locale.

#### Improvements on localization setup

For people with poor quality or spotty network access who are not able to download language packs in the startup step, we made two changes on the client side.

- Prefetch is kicked off in existing client builds before the new client version is released. A background task is scheduled to download the language pack file based on the new version and app language.
- Fallback: The majority of the translations don’t change from version to version. In the localization initialization step, we load a stale language pack file if the target language pack version is not available. In this session, a background task is scheduled to fetch the target language pack version.

For both improvements, people using the app have higher chances of getting the latest translations in the next session without interrupting user experience.

## Performance on Facebook App

Downloading on-demand language packs is a reliable infra solution that supports more languages and saves on app size simultaneously; users will only download the language pack file they are going to utilize. Let’s check some data points that show infrastructure efficiency and end-user experience based on the Facebook app. The download size of each language pack varies from 600KB to 2MB depending on the language. For Facebook on iOS, the success rate of loading this infra is over 99.99 percent. Over 99.8 percent of people load language packs from disk and the average loading time is around 80ms. For Facebook for Android, the loading success rate is over 99.7 percent. The average time to load a language pack file from a disk is around 780ms across all device classes. Based on our measurements over half of the year, downloading language packs didn’t show a negative impact on startup and overall Facebook App critical metrics.

## Integrating language packs at Meta scale

While this solution has worked well for Facebook and Workplace, the language packs framework is not a one size fits all solution. For example, for apps that don’t require many translations or that are sensitive to startup performance, bundled language packs might be a better option. In order to tackle our next challenge — integrating this localization framework across the company — we’ll need to consider which solutions will best suit each of our apps.

We continue to explore new ways to deliver high-quality localized experiences to enable people in different countries and regions to connect with one another. We’ve opened up the Javascript FBT GitHub repository for public access at [facebook.github.io/fbt/](https://facebook.github.io/fbt/) so anyone can learn about FBT.

_Thanks to everyone who contributed to the FBT framework and language packs._
