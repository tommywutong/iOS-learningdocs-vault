---
title: A Geocoding Service for OS X
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/01/geocoding-automator-service/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:85f258c98c61333e'
translated: false
---

> 原文：[A Geocoding Service for OS X](https://oleb.net/blog/2014/01/geocoding-automator-service/)　·　Ole Begemann

# A Geocoding Service for OS X

[![My geocoding service for OS X in action](https://oleb.net/media/geocoding-workflow-demo-screencast.gif)](https://oleb.net/media/geocoding-workflow-demo-screencast.gif)

When I work on an app with location-based features, I often need the geo coordinates of a specific place for testing. Since it’s surprisingly difficult to view a location’s coordinates in Google Maps (let alone copy them in the correct format), I used to get them from a place’s page on Wikipedia, but it became a bit tedious over time.

# Ruby Geocoder Gem

I started looking for a better way and found Alex Reisner’s fantastic [Ruby Geocoder](http://www.rubygeocoder.com) gem. It comes with a command line interface that works like this:

```
> [sudo] gem install geocoder
Fetching: geocoder-1.1.9.gem (100%)
Successfully installed geocoder-1.1.9
1 gem installed

> geocode "Alexanderplatz, Berlin"
Latitude:         52.521642
Longitude:        13.411007
Full address:     Berlin Alexanderplatz (S), 10178 Berlin, Germany
City:             Berlin
State/province:   Berlin
Postal code:      10178
Country:          Germany
Google map:       http://maps.google.com/maps?q=52.521642,13.411007
```

This is great, but copying and pasting the coordinates into code still requires multiple steps. So I wrote a little script that directly uses the geocoder’s Ruby API and prints the coordinates in the format I need to pass them to [`CLLocationCoordinate2DMake()`](https://developer.apple.com/library/ios/documentation/CoreLocation/Reference/CoreLocationFunctions/Reference/reference.html#//apple_ref/doc/uid/TP40009576-CH2-SW4):

```
> ./geocode_coordinates.rb "Alexanderplatz, Berlin"
52.521642, 13.411007
```

The script takes its inputs either from the command line or from stdin. You can [download it from GitHub](https://gist.github.com/ole/8583982).

# An Automator Service for OS X

We can further improve the workflow by turning the script into a service for OS X that works on the currently selected text. We can do this with Automator. [Download the workflow](https://oleb.net/media/Geocode.workflow.zip).^[1](#fn:1)

After you have installed the service, select one or multiple place names or addresses (one per line) in any app and choose _[App Name] \> Services \> Geocode_ to replace the selection with the resulting coordinates. You can assign a keyboard shortcut to the service in _System Preferences \> Keyboard \> Shortcuts_.

[![My geocoding service for OS X in action](https://oleb.net/media/geocoding-workflow-demo-screencast-2.gif)](https://oleb.net/media/geocoding-workflow-demo-screencast-2.gif)

Keep in mind that you still need to install the Ruby Geocoder gem before you can run the Automator workflow. If you use a Ruby version manager such as rbenv or RVM, make sure to install the gem under the system’s Ruby installation. For example in rbenv:

```
> rbenv global system
> sudo gem install geocoder
```

1. The service is not code signed, so if you have Gatekeeper enabled, you need to open it through the context menu. I could not figure out how to apply a working Developer ID signature to an Automator service. Automator itself only offers the option to code sign on export for workflows that are packaged as app bundles. And `codesign -s "Developer ID Application: Ole Begemann" --deep Geocode.workflow` seems to work fine but Gatekeeper still prevents the opening. I’d be grateful for any tips. [↩︎](#fnref:1)
