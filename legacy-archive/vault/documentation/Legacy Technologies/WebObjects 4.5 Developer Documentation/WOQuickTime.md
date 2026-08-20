---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOQuickTime.html
archived_at: '2026-07-15T08:09:53.441300Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOQuickTime

## Element Description

WOQuickTime is a dynamic element that you can use to incorporate
QuickTime objects (movie, sound, VR, ...) into your WebObjects applications.
The WOQuickTime API is essentially based on the QuickTime plug-ins
API.

WOQuickTime supports QuickTime VR with hotspots. If you specify
a list of hotspots and the user clicks inside the QuickTime VR object,
the method specified by the __action__ attribute
is performed and the __selection__ attribute
is set to the value of the selected hotspot.

You should use WOQuickTime components outside of an HTML form.

## Synopsis

WOQuickTime { filename=_imageFilePath_;
| src=_aURL_; | [framework=_frameworkName_ |
"app";] width=_anInt_; height=_anInt_;
[hidden=_aBoolean_;] [pluginsPage=_aURL_;]
[hotspotList=_arrayOfIDs_; selection=_aString_;
action=_aMethod_; href=_anHREF_;
| pageName=_page_; [target=_frameTarget_;]] [bgcolor=_hexString_;]
[volume=_anInt_;] [pan=_panAngle_;]
[tilt=_tiltAngle_;] [fov=_fieldOfView_;] [node=_initialNode_;]
[correction=NONE|PARTIAL|FULL;] [cache=_aBoolean_;]
[autoplay=_aBoolean_;] [playeveryframe=_aBoolean_;]
[controller=_aBoolean_;] [prefixhost=_aBoolean_;]

## Bindings

WOQuickTime has the following attributes. Those attributes
relevant only to VR movies are indicated with "[VR]" in the
description.

**filename**
: Path to the QuickTime object relative to the WebServerResources
directory.

**src**
: URL locating the QuickTime object. Use this attribute
for complete URLs; for relative URLs use __filename__ instead.

**framework**
: The framework that contains the QuickTime object. This
attribute is only necessary if the QuickTime object is in a different
location from the component. That is, if the component and the QuickTime
object are both in the application or if the component and the QuickTime object
are both in the same framework, this attribute isn't necessary.
If the QuickTime object is in a framework and the component is in
the application, specify the framework's name here (minus the `.framework` extension).
If the QuickTime object should be in the application but the component
is in a framework, specify the `"app"` keyword
in place of the framework name.

**width**
: QuickTime object width in pixels. The __width__ attribute
is required. Never specify a width of less than 2 as this can cause
problems with some browsers. If you are trying to hide the movie,
use the __hidden__ attribute instead. If you
don't know the width of the movie, open your movie with MoviePlayer
(it comes with QuickTime) and select Get Info from the Movie menu.
If you don't use the __scale__ attribute
and you supply a width that is smaller than the actual width of
the movie, the movie will be cropped to fit. If you supply a width
that is greater than the width of the movie, the movie will be centered
inside this width.

**height**
: Quicktime object height in pixels. If you want to display
the movie's controller, you'll need to add 16 pixels to the
height. __height__ is required unless you use
the __hidden__ attribute. Never specify a height
of less than 2 as this can cause problems with some browsers. If
you are trying to hide the movie, use the __hidden__ attribute
instead. If you don't know the height of the movie, open your movie
with MoviePlayer and select Get Info from the Movie menu. If you
do not use the __scale__ attribute and you
supply a height that is smaller than the actual height of the movie
(plus 16 if you are showing the controller), the movie will be cropped
to fit. If you supply a height that is greater than the height of
the movie, the movie will be centered inside this height.

**pluginsPage**
: This optional attribute allows you to specify a URL
from which the user can fetch the necessary plug-in if it is not
installed. This attribute is handled by your browser. If your browser
cannot find the plug-in when loading your page, it will warn the
user and allow them to bring up the specified URL. Generally this
parameter should be set to "`http://www.apple.com/quicktime`".
This attribute is appropriate for both QuickTime movies and QuickTime
VR Objects and Panoramas.

**hotspotList**
: [VR] The hotspot list is an array of strings, each of
which should be mapped to a hotspot ID as defined when the hotspots
are created with the QuickTime VR authoring tools.

**selection**
: [VR] A string corresponding to the ID of the user-selected
hotspot or `nil` if none is selected.

**action**
: Method to invoke when the QuickTime object is clicked.
The selection parameter then contains the ID of the selected hotspot
if a hotspot list has been specified, or `nil` otherwise.

**href**
: An optional attribute for specifying a URL to direct
the browser to when the QuickTime object is clicked and no hotspots
are hit.

**pageName**
: An optional attribute specifying the name of the WebObjects
page to display when the QuickTime object is clicked and no hotspots
are hit.

**bgcolor**
: Background color for the QuickTime object. This is an
optional attribute. Use __bgcolor__ to specify
the background color for any space that is not taken by the movie\xF6as,
for example, if you embed a 160x120 movie in a 200x120 space. Specify
the color as a hex value.

**target**
: (optional) When set, the __target__ attribute
is the name of a valid frame (including `_self`, `_top`, `_parent`, `_blank` or
an explicit frame name) that will be the target of a link specified
by the hotspot or `href` attribute.

**volume**
: An optional attribute affecting the initial volume level.
Possible values are 0 through 100. A setting of 0 effectively mutes
the audio; a setting of 100 is maximum volume.

**pan**
: [VR] This optional attribute allows you to specify the
initial pan angle for a QuickTime VR movie.The range of values for
a typical movie would be 0.0 to 360.0 degrees. If no value for __pan__ is
specified, the value stored in the movie is used.

**tilt**
: [VR] This optional attribute allows you to specify the
initial tilt angle for a QuickTime VR movie. The range of values
for a typical movie would be -42.5 to 42.5 degrees. If no value for __tilt__ is
specified, the value stored in the movie is used.

**fov**
: [VR] This optional attribute allows you to specify the
initial field of view angle for a QuickTime VR movie.The range of
values for a typical movie would be 5.0 to 85.0 degrees. If no value
is specified for __fov__, the value stored
in the panoramic movie is used.

**node**
: [VR] This optional attribute allows you to specify the
initial node for a multi-node QuickTime VR movie. If no value is
specified for __node__ , the default node and
view (specified at creation time of the movie) is used.

**correction**
: [VR] (optional) Possible values are "`NONE`",
"`PARTIAL`", or "`FULL`"
(the default). This attribute is only appropriate for QuickTime
VR objects and panoramas.

**cache**
: (optional) If __cache__ evaluates
to `true` (or `YES`),
the browser will cache movies when possible just like other documents.

**autoplay**
: (optional) When __autoplay__ evaluates
to `true` (or `YES`),
causes the movie to start playing as soon as the QuickTime Plug-In
estimates that it'll be able to play the entire movie without waiting
for additional data. This attribute's default is specified by
a user setting in the QuickTime Plug-in Preferences.

**hidden**
: This optional attribute controls the visibility of the
movie. By default the value is `true` (or `YES`);
if you set it to `false` (or `NO`)
the movie won't be visible on the page. This option is not appropriate
for QuickTime VR Objects or Panoramas. You can use __hidden__ to
hide a sound-only movie.

**playEveryFrame**
: When this optional attribute evaluates to `true` (or `YES`)
the QuickTime plug-in plays every frame, even if it is necessary
to play at a slower rate to do so. This attribute is particularly useful
to play simple animations, and is appropriate for QuickTime movies.
Note that enabling __playEveryFrame__ will
turn off any audio tracks your movie may have.

**controller**
: This optional attribute sets the visibility of the movie
controller (with QTVR 2.1, you can have a controller on VR Panarama
or Object Movies). If you don't specify __controller__,
the default is `true` (or `YES`)
for QuickTime movies. For compatibility with existing web pages, the
default is `false` (or `NO`)
for QuickTime VR movies.

**prefixHost**
: This attribute should be used to fix a bug with the
QuickTime 2.x plug-in on Windows platforms. Setting __prefixHost__ to `true` (or `YES`)
will automatically add the http host name at the beginning of each
dynamic URL, allowing old plug-ins to correctly handle WOQuickTime
component. The default is `false` (or `NO`)

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
