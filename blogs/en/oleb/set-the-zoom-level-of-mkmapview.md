---
title: Set the Zoom Level of MKMapView
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/05/set-the-zoom-level-of-mkmapview/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:71466331ef7f86d7'
translated: false
---

> 原文：[Set the Zoom Level of MKMapView](https://oleb.net/blog/2010/05/set-the-zoom-level-of-mkmapview/)　·　Ole Begemann

# Set the Zoom Level of MKMapView

A [very nice MKMapView category](http://troybrant.net/blog/2010/01/set-the-zoom-level-of-an-mkmapview/) by Troy Brant that allows you to zoom the map by settting the zoom level (as in the [Javascript Google Maps API](https://code.google.com/apis/maps/)) in addition to Apple’s way of zooming by modifying the map’s region:

> Unfortunately, MapKit on the iPhone does not include a way to set the zoom level. Instead, the zoom level is set implicitly by defining the `MKCoordinateRegion` of the map’s viewport. When initializing the region, you specify the amount of distance the map displays in the horizontal and vertical directions. The zoom level is set implicitly based on these distance values. Instead of dealing with this region business, I wrote a category that adds support for setting the zoom level of an `MKMapView` explicitly.

Troy also wrote an [extensively detailed post on the mathematical background](http://troybrant.net/blog/2010/01/mkmapview-and-zoom-levels-a-visual-guide/) of his code. Great stuff!
