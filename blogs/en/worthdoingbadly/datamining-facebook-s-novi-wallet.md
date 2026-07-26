---
title: Datamining Facebook’s Novi wallet
source: worthdoingbadly (Zhuowei Zhang)
source_key: worthdoingbadly
source_url: 'https://worthdoingbadly.com/novi/'
original_language: en
published: 2021-11-23
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9344fb11819d9908'
translated: false
---

> 原文：[Datamining Facebook’s Novi wallet](https://worthdoingbadly.com/novi/)　·　worthdoingbadly (Zhuowei Zhang)

# Datamining Facebook's Novi wallet

Nov 23, 2021

I tested Facebook’s new [Novi](https://novi.com) digital wallet and found evidence for upcoming features, such as a debit card to access Novi balance, third-party linking with QR codes, and a way to buy Bitcoin directly from the app.

![A screenshot of Novi](https://worthdoingbadly.com/assets/blog/novi/novi.jpg)

# A hands-on video! Sort of.

Here’s my “hands-on” of the Novi settings screen on Android. I can’t demo the actual wallet since I wasn’t able to sign up for an account.

[https://twitter.com/zhuowei/status/1457420727838195728](https://twitter.com/zhuowei/status/1457420727838195728)

> Facebook Novi wallet hands-on:  
> ... except I'm not going to give Facebook my driver's license or bank account  
> You only get to see an empty "Settings" screen. Sorry. [pic.twitter.com/Grh9Fhz22J](https://t.co/Grh9Fhz22J)
> 
> — Zhuowei Zhang (@zhuowei) [November 7, 2021](https://twitter.com/zhuowei/status/1457420727838195728?ref_src=twsrc%5Etfw)

I wasn’t eligible for the Novi beta (which requires you to be a resident of selected states in the US or Guatamala, and requires you to upload your photo ID).

To work around this, I:

- rented a cloud server in California
- modified the APK to replace “prod.novi.com” with my own server
- disabled certificate pinning by adding a `return-void` to the function that throws the `pinning error, trusted chain:` error.
- changed `kyc_status` in the login response to `ONBOARDED`

This allowed me to view… the settings screen, and that’s it. (The actual money UI is controlled by the server, and without a valid account, it just gives a blank homescreen)

# Enabling feature flags in Novi’s Android app

[https://twitter.com/zhuowei/status/1457420727838195728](https://twitter.com/zhuowei/status/1457420727838195728)

![](https://pbs.twimg.com/media/FCgce3tWYAYplPh?format=jpg)

[https://twitter.com/zhuowei/status/1457428236774817796](https://twitter.com/zhuowei/status/1457428236774817796)

If I enable every unreleased experiment flag in Facebook’s Novi wallet, I get a few extra settings for “Statements and Documents”, “Diem address”, “Sounds”, and “Linked accounts”:

| ![](https://pbs.twimg.com/media/FDnTQA_XEAISxcU?format=jpg) | ![](https://pbs.twimg.com/media/FDnTQDIXsAQawCl?format=jpg) |
|---|---|
| ![](https://pbs.twimg.com/media/FDnTQH5WUAUZql_?format=jpg) | ![](https://pbs.twimg.com/media/FDnTQKJXsBAHNTS?format=jpg) |

# Strings

I also pulled strings from both the Android and the iOS versions of the app:

## Novi Card

Facebook’s Novi digital wallet includes text about a “Novi Card”, a Visa-compatible debit card to access your Novi balance:

[https://twitter.com/zhuowei/status/1451644426221015041](https://twitter.com/zhuowei/status/1451644426221015041)

![](https://pbs.twimg.com/media/FCVG6SWXsAgK7qS?format=jpg)

## QR linking

Facebook’s Novi wallet seems to let you link an account with a third party by scanning a QR code? I’m not sure what kind of third party this would support.

[https://twitter.com/zhuowei/status/1451648546827030531](https://twitter.com/zhuowei/status/1451648546827030531)

![](https://pbs.twimg.com/media/FCVKqLzXEA0Rx-z?format=jpg)

## Buying Bitcoin

Facebook’s Novi wallet has text about… buying Bitcoin, for some reason:

[https://twitter.com/zhuowei/status/1451647713150480390](https://twitter.com/zhuowei/status/1451647713150480390)

![](https://pbs.twimg.com/media/FCVJ5p5WYAQYUH-?format=jpg)

## Android strings

Here’s the [strings.xml](https://gist.github.com/zhuowei/fb37eddd1808f31786855f3e3b847b5e) of the Novi Android APK if you want to see if there’s anything else interesting.

[https://worthdoingbadly.com/novi/](https://worthdoingbadly.com/novi/)
