---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/ManipulateImages.html
archived_at: '2026-07-15T07:45:48.461028Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Manipulating Images

Image Events is a scriptable background app in OS X that can be used to automate the manipulation of images without the need for a fully-featured image editor. You can use Image Events to:

- Read image properties
- Flip and rotate images
- Crop and add padding to images
- Resize images
- Convert images from one type to another

The Image Events app is located in `/System/Library/CoreServices/`. You can access its dictionary from the Library palette in Script Editor. See [Opening a Scripting Dictionary](OpenaScriptingDictionary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnzwfvjvomi).

> [!NOTE]
> 

### The Image Events Workflow

To manipulate an image with Image Events, a script typically performs the following sequential steps:

1. Open the Image Events app.
2. Open an image file.
3. Access image properties or manipulate the image.
4. Save the modified image as a new image file or overwriting the original image file.
5. Close the image.

### Opening an Image

An image must be opened before Image Events can interact with it. To open an image, use the `open` command and provide the image’s path, as shown in Listing 38-1.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=--%20Prompt%20for%20an%20image%0Aset%20theImageFile%20to%20choose%20file%20of%20type%20%22public.image%22%20with%20prompt%20%22%22%0A%0A--%20Launch%20Image%20Events%20and%20open%20the%20image%0Atell%20application%20%22Image%20Events%22%0A%20%20%20%20launch%0A%20%20%20%20open%20theImageFile%0Aend%20tell%0A--%3E%20Result%3A%20image%20%22My%20Image.png%22%20of%20application%20%22Image%20Events%22)

__Listing 38-1__AppleScript: Opening an image with Image Events

1. `-- Prompt for an image`
2. `set theImageFile to choose file of type "public.image" with prompt ""`
4. `-- Launch Image Events and open the image`
5. `tell application "Image Events"`
6. `launch`
7. `open theImageFile`
8. `end tell`
9. `--> Result: image "My Image.png" of application "Image Events"`

The result of the open command is an `image` object, the newly opened image. Since Image Events is a background app, opening an image produces no visible changes onscreen—you won’t actually _see_ the opened image.

> [!NOTE]
> 

### Reading Image Properties

Like all scriptable objects, images have attributes that define them, such as dimensions, color space, and resolution. The `image` class in the Image Events scripting dictionary contains a variety of properties for key attributes. Listing 38-2 shows how to access some of these properties. First, it retrieves a record of available properties for a selected image. Next, it retrieves some individual properties.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=--%20Prompt%20for%20an%20image%0Aset%20theImageFile%20to%20choose%20file%20of%20type%20%22public.image%22%20with%20prompt%20%22%22%0A%0A--%20Launch%20Image%20Events%0Atell%20application%20%22Image%20Events%22%0A%20%20%20%20launch%0A%0A%20%20%20%20--%20Open%20the%20image%0A%20%20%20%20set%20theImage%20to%20open%20theImageFile%0A%0A%20%20%20%20--%20Read%20the%20image%27s%20properties%0A%20%20%20%20tell%20theImage%0A%20%20%20%20%20%20%20%20properties%0A%20%20%20%20%20%20%20%20--%3E%20%7Bcolor%20space%3ARGB%2C%20image%20file%3Afile%20%22Macintosh%20HD%3AUsers%3AYourUserName%3ADesktop%3AMy%20Image.png%22%20of%20application%20%22Image%20Events%22%2C%20bit%20depth%3Amillions%20of%20colors%2C%20dimensions%3A%7B293%2C%20252%7D%2C%20location%3Afolder%20%22Macintosh%20HD%3AUsers%3AYourUserName%3ADesktop%3A%22%20of%20application%20%22Image%20Events%22%2C%20embedded%20profile%3Aprofile%20%22Thunderbolt%20Display%22%20of%20image%20%22My%20Image.png%22%20of%20application%20%22Image%20Events%22%2C%20file%20type%3APNG%2C%20class%3Aimage%2C%20name%3A%22My%20Image.png%22%2C%20resolution%3A%7B72.0%2C%2072.0%7D%7D%0A%0A%20%20%20%20%20%20%20%20--%20Read%20the%20image%27s%20resolution%0A%20%20%20%20%20%20%20resolution%0A%20%20%20%20%20%20%20%20--%3E%20%7B72.0%2C%2072.0%7D%0A%0A%20%20%20%20%20%20%20%20--%20Read%20the%20image%27s%20type%0A%20%20%20%20%20%20%20file%20type%0A%20%20%20%20%20%20%20%20--%3E%20PNG%0A%0A%20%20%20%20%20%20%20%20--%20Read%20the%20name%20of%20the%20image%27s%20embedded%20profile%0A%20%20%20%20%20%20%20name%20of%20embedded%20profile%0A%20%20%20%20%20%20%20%20--%3E%20%22Thunderbolt%20Display%22%0A%20%20%20%20end%20tell%0Aend%20tell)

__Listing 38-2__AppleScript: Retrieving properties from an image

1. `-- Prompt for an image`
2. `set theImageFile to choose file of type "public.image" with prompt ""`
4. `-- Launch Image Events`
5. `tell application "Image Events"`
6. `launch`
8. `-- Open the image`
9. `set theImage to open theImageFile`
11. `-- Read the image's properties`
12. `tell theImage`
13. `properties`
14. `--> {color space:RGB, image file:file "Macintosh HD:Users:YourUserName:Desktop:My Image.png" of application "Image Events", bit depth:millions of colors, dimensions:{293, 252}, location:folder "Macintosh HD:Users:YourUserName:Desktop:" of application "Image Events", embedded profile:profile "Thunderbolt Display" of image "My Image.png" of application "Image Events", file type:PNG, class:image, name:"My Image.png", resolution:{72.0, 72.0}}`
16. `-- Read the image's resolution`
17. `resolution`
18. `--> {72.0, 72.0}`
20. `-- Read the image's type`
21. `file type`
22. `--> PNG`
24. `-- Read the name of the image's embedded profile`
25. `name of embedded profile`
26. `--> "Thunderbolt Display"`
27. `end tell`
28. `end tell`

### Flipping an Image

The `flip` command reverses the axis of an image. It has two options for the required parameter: `horizontal` for changing the axis of the image on a horizontal plane, and `vertical` for changing the axis of the image on a vertical plane. Listing 38-3 flips an image both horizontally and vertically.

> [!IMPORTANT]
> 

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=--%20Prompt%20for%20an%20image%0Aset%20theImageFile%20to%20choose%20file%20of%20type%20%22public.image%22%20with%20prompt%20%22%22%0A%0A--%20Locate%20an%20output%20folder%0Aset%20theOutputFolder%20to%20%28path%20to%20desktop%20folder%20as%20string%29%0A%0A--%20Launch%20Image%20Events%0Atell%20application%20%22Image%20Events%22%0A%20%20%20%20launch%0A%0A%20%20%20%20--%20Open%20the%20image%0A%20%20%20%20set%20theImage%20to%20open%20theImageFile%0A%20%20%20%20tell%20theImage%0A%0A%20%20%20%20%20%20%20%20--%20Determine%20a%20save%20name%20for%20the%20image%0A%20%20%20%20%20%20%20%20set%20theName%20to%20name%0A%20%20%20%20%20%20%20%20set%20theSaveName%20to%20%22temp-%22%20%26%20theName%0A%0A%20%20%20%20%20%20%20%20--%20Flip%20the%20image%20horizontally%0A%20%20%20%20%20%20%20%20flip%20with%20horizontal%0A%0A%20%20%20%20%20%20%20%20--%20Flip%20the%20image%20vertically%0A%20%20%20%20%20%20%20%20flip%20with%20vertical%0A%0A%20%20%20%20%20%20%20%20--%20Save%20the%20image%20to%20the%20output%20folder%2C%20using%20the%20save%20name%0A%20%20%20%20%20%20%20%20save%20as%20file%20type%20in%20%28theOutputFolder%20%26%20theSaveName%29%0A%0A%20%20%20%20%20%20%20%20--%20Close%20the%20image%0A%20%20%20%20%20%20%20%20close%0A%20%20%20%20end%20tell%0Aend%20tell)

__Listing 38-3__AppleScript: Flipping an image

1. `-- Prompt for an image`
2. `set theImageFile to choose file of type "public.image" with prompt ""`
4. `-- Locate an output folder`
5. `set theOutputFolder to (path to desktop folder as string)`
7. `-- Launch Image Events`
8. `tell application "Image Events"`
9. `launch`
11. `-- Open the image`
12. `set theImage to open theImageFile`
13. `tell theImage`
15. `-- Determine a save name for the image`
16. `set theName to name`
17. `set theSaveName to "temp-" & theName`
19. `-- Flip the image horizontally`
20. `flip with horizontal`
22. `-- Flip the image vertically`
23. `flip with vertical`
25. `-- Save the image to the output folder, using the save name`
26. `save as file type in (theOutputFolder & theSaveName)`
28. `-- Close the image`
29. `close`
30. `end tell`
31. `end tell`

### Rotating an Image

The `rotate` command rotates an image around its center point. To rotate an image clockwise, provide the command’s `to angle` parameter with an integer value between `1` to `359` (see Listing 38-4). To rotate an image counter-clockwise, provide a negative value, such as `-90`.

> [!IMPORTANT]
> 

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=--%20Prompt%20for%20an%20image%0Aset%20theImageFile%20to%20choose%20file%20of%20type%20%22public.image%22%20with%20prompt%20%22%22%0A%0A--%20Locate%20an%20output%20folder%0Aset%20theOutputFolder%20to%20%28path%20to%20desktop%20folder%20as%20string%29%0A%0A--%20Launch%20Image%20Events%0Atell%20application%20%22Image%20Events%22%0A%20%20%20%20launch%0A%0A%20%20%20%20--%20Open%20the%20image%0A%20%20%20%20set%20theImage%20to%20open%20theImageFile%0A%20%20%20%20tell%20theImage%0A%0A%20%20%20%20%20%20%20%20--%20Determine%20a%20save%20name%20for%20the%20image%0A%20%20%20%20%20%20%20%20set%20theName%20to%20name%0A%20%20%20%20%20%20%20%20set%20theSaveName%20to%20%22temp-%22%20%26%20theName%0A%0A%20%20%20%20%20%20%20%20--%20Rotate%20an%20image%2045%20degrees%0A%20%20%20%20%20%20%20%20rotate%20to%20angle%2045%0A%0A%20%20%20%20%20%20%20%20--%20Save%20the%20image%20to%20the%20output%20folder%2C%20using%20the%20save%20name%0A%20%20%20%20%20%20%20%20save%20as%20file%20type%20in%20%28theOutputFolder%20%26%20theSaveName%29%0A%0A%20%20%20%20%20%20%20%20--%20Close%20the%20image%0A%20%20%20%20%20%20%20%20close%0A%20%20%20%20end%20tell%0Aend%20tell)

__Listing 38-4__AppleScript: Rotating an image

1. `-- Prompt for an image`
2. `set theImageFile to choose file of type "public.image" with prompt ""`
4. `-- Locate an output folder`
5. `set theOutputFolder to (path to desktop folder as string)`
7. `-- Launch Image Events`
8. `tell application "Image Events"`
9. `launch`
11. `-- Open the image`
12. `set theImage to open theImageFile`
13. `tell theImage`
15. `-- Determine a save name for the image`
16. `set theName to name`
17. `set theSaveName to "temp-" & theName`
19. `-- Rotate an image 45 degrees`
20. `rotate to angle 45`
22. `-- Save the image to the output folder, using the save name`
23. `save as file type in (theOutputFolder & theSaveName)`
25. `-- Close the image`
26. `close`
27. `end tell`
28. `end tell`

### Scaling an Image

Scaling an image proportionally increases or decreases its dimensions. The `scale` command can resize images in one of two ways:

- To scale an image by percentage, provide a decimal value for the `by factor` parameter. The value `1` is equivalent to 100%. The value `.5` is 50%. The value `1.5` is 150% and so on.

  Use the following formula to determine the scaling factor:

  `«percentage» * .01`
- To scale an image to a specific size, provide an integer value for the `to size` parameter. This value indicates the maximum number of pixels for the resized image on its longest side.

Scaling doesn’t change the resolution of an image. For example, a 72 dpi image that has been scaled to 50% of its original dimensions still has a resolution of 72 dpi.

Listing 38-5 demonstrates how to resize an image. It can scale by percentage or pixels, depending on the value of a Boolean variable.

> [!IMPORTANT]
> 

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=--%20Prompt%20for%20an%20image%0Aset%20theImageFile%20to%20choose%20file%20of%20type%20%22public.image%22%20with%20prompt%20%22%22%0A%0A--%20Locate%20an%20output%20folder%0Aset%20theOutputFolder%20to%20%28path%20to%20desktop%20folder%20as%20string%29%0A%0A--%20To%20scale%20by%20percentage%2C%20set%20this%20value%20to%20true.%20To%20scale%20to%20a%20specific%20size%2C%20set%20it%20to%20false.%0Aset%20scaleByPercentage%20to%20true%0A%0A--%20Launch%20Image%20Events%0Atell%20application%20%22Image%20Events%22%0A%20%20%20%20launch%0A%0A%20%20%20%20--%20Open%20the%20image%0A%20%20%20%20set%20theImage%20to%20open%20theImageFile%0A%20%20%20%20tell%20theImage%0A%0A%20%20%20%20%20%20%20%20--%20Determine%20a%20save%20name%20for%20the%20image%0A%20%20%20%20%20%20%20%20set%20theName%20to%20name%0A%20%20%20%20%20%20%20%20set%20theSaveName%20to%20%22temp-%22%20%26%20theName%0A%0A%20%20%20%20%20%20%20%20--%20Scale%20the%20image%20by%2050%25%0A%20%20%20%20%20%20%20%20if%20scaleByPercentage%20%3D%20true%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20scale%20by%20factor%200.5%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20--%20Scale%20the%20image%20to%20100px%20on%20its%20longese%20side%0A%20%20%20%20%20%20%20%20else%0A%20%20%20%20%20%20%20%20%20%20%20%20scale%20to%20size%20100%0A%20%20%20%20%20%20%20%20end%20if%0A%0A%20%20%20%20%20%20%20%20--%20Save%20the%20image%20to%20the%20output%20folder%2C%20using%20the%20save%20name%0A%20%20%20%20%20%20%20%20save%20as%20file%20type%20in%20%28theOutputFolder%20%26%20theSaveName%29%0A%0A%20%20%20%20%20%20%20%20--%20Close%20the%20image%0A%20%20%20%20%20%20%20%20close%0A%20%20%20%20end%20tell%0Aend%20tell)

__Listing 38-5__AppleScript: Scaling an image

1. `-- Prompt for an image`
2. `set theImageFile to choose file of type "public.image" with prompt ""`
4. `-- Locate an output folder`
5. `set theOutputFolder to (path to desktop folder as string)`
7. `-- To scale by percentage, set this value to true. To scale to a specific size, set it to false.`
8. `set scaleByPercentage to true`
10. `-- Launch Image Events`
11. `tell application "Image Events"`
12. `launch`
14. `-- Open the image`
15. `set theImage to open theImageFile`
16. `tell theImage`
18. `-- Determine a save name for the image`
19. `set theName to name`
20. `set theSaveName to "temp-" & theName`
22. `-- Scale the image by 50%`
23. `if scaleByPercentage = true then`
24. `scale by factor 0.5`
26. `-- Scale the image to 100px on its longese side`
27. `else`
28. `scale to size 100`
29. `end if`
31. `-- Save the image to the output folder, using the save name`
32. `save as file type in (theOutputFolder & theSaveName)`
34. `-- Close the image`
35. `close`
36. `end tell`
37. `end tell`

### Cropping an Image

Cropping an image removes pixels around all of its sides, centering the remaining area. The `to dimensions` required parameter takes a list of two integers: the new width and height, in pixels. In Listing 38-6, an image is cropped to 100 by 100 pixels.

> [!IMPORTANT]
> 

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=--%20Prompt%20for%20an%20image%0Aset%20theImageFile%20to%20choose%20file%20of%20type%20%22public.image%22%20with%20prompt%20%22%22%0A%0A--%20Locate%20an%20output%20folder%0Aset%20theOutputFolder%20to%20%28path%20to%20desktop%20folder%20as%20string%29%0A%0A--%20Launch%20Image%20Events%0Atell%20application%20%22Image%20Events%22%0A%20%20%20%20launch%0A%0A%20%20%20%20--%20Open%20the%20image%0A%20%20%20%20set%20theImage%20to%20open%20theImageFile%0A%20%20%20%20tell%20theImage%0A%0A%20%20%20%20%20%20%20%20--%20Determine%20a%20save%20name%20for%20the%20image%0A%20%20%20%20%20%20%20%20set%20theName%20to%20name%0A%20%20%20%20%20%20%20%20set%20theSaveName%20to%20%22temp-%22%20%26%20theName%0A%0A%20%20%20%20%20%20%20%20--%20Crop%20the%20image%20to%20100px%20by%20100px%0A%20%20%20%20%20%20%20%20crop%20to%20dimensions%20%7B100%2C%20100%7D%0A%0A%20%20%20%20%20%20%20%20--%20Save%20the%20image%20to%20the%20output%20folder%2C%20using%20the%20save%20name%0A%20%20%20%20%20%20%20%20save%20as%20file%20type%20in%20%28theOutputFolder%20%26%20theSaveName%29%0A%0A%20%20%20%20%20%20%20%20--%20Close%20the%20image%0A%20%20%20%20%20%20%20%20close%0A%20%20%20%20end%20tell%0Aend%20tell)

__Listing 38-6__AppleScript: Cropping an image

1. `-- Prompt for an image`
2. `set theImageFile to choose file of type "public.image" with prompt ""`
4. `-- Locate an output folder`
5. `set theOutputFolder to (path to desktop folder as string)`
7. `-- Launch Image Events`
8. `tell application "Image Events"`
9. `launch`
11. `-- Open the image`
12. `set theImage to open theImageFile`
13. `tell theImage`
15. `-- Determine a save name for the image`
16. `set theName to name`
17. `set theSaveName to "temp-" & theName`
19. `-- Crop the image to 100px by 100px`
20. `crop to dimensions {100, 100}`
22. `-- Save the image to the output folder, using the save name`
23. `save as file type in (theOutputFolder & theSaveName)`
25. `-- Close the image`
26. `close`
27. `end tell`
28. `end tell`

### Padding an Image

Padding an image adds space around its sides. It’s essentially the reverse of cropping an image, although negative padding an image produces cropping. The `to dimensions` required parameter takes a list of two integers: the new width and height, in pixels. The optional `with pad color` parameter can be used to specify the color of the padding. In Listing 38-7, 20 pixels of padding is added around an image.

> [!IMPORTANT]
> 

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=--%20Prompt%20for%20an%20image%0Aset%20theImageFile%20to%20choose%20file%20of%20type%20%22public.image%22%20with%20prompt%20%22%22%0A%0A--%20Prompt%20for%20a%20color%0Aset%20theColor%20to%20choose%20color%0A%0A--%20Locate%20an%20output%20folder%0Aset%20theOutputFolder%20to%20%28path%20to%20desktop%20folder%20as%20string%29%0A%0A--%20Launch%20Image%20Events%0Atell%20application%20%22Image%20Events%22%0A%20%20%20%20launch%0A%0A%20%20%20%20--%20Open%20the%20image%0A%20%20%20%20set%20theImage%20to%20open%20theImageFile%0A%20%20%20%20tell%20theImage%0A%0A%20%20%20%20%20%20%20%20--%20Determine%20a%20save%20name%20for%20the%20image%0A%20%20%20%20%20%20%20%20set%20theName%20to%20name%0A%20%20%20%20%20%20%20%20set%20theSaveName%20to%20%22temp-%22%20%26%20theName%0A%0A%20%20%20%20%20%20%20%20--%20Get%20the%20current%20dimensions%20of%20the%20image%0A%20%20%20%20%20%20%20%20set%20%7BtheWidth%2C%20theHeight%7D%20to%20dimensions%0A%0A%20%20%20%20%20%20%20%20--%20Pad%20the%20image%20by%2020%20pixels%20on%20all%20sides%0A%20%20%20%20%20%20%20%20pad%20to%20dimensions%20%7BtheWidth%20%2B%2020%2C%20theHeight%20%2B%2020%7D%20with%20pad%20color%20theColor%0A%0A%20%20%20%20%20%20%20%20--%20Save%20the%20image%20to%20the%20output%20folder%2C%20using%20the%20save%20name%0A%20%20%20%20%20%20%20%20save%20as%20file%20type%20in%20%28theOutputFolder%20%26%20theSaveName%29%0A%0A%20%20%20%20%20%20%20%20--%20Close%20the%20image%0A%20%20%20%20%20%20%20%20close%0A%20%20%20%20end%20tell%0Aend%20tell)

__Listing 38-7__AppleScript: Padding an image

1. `-- Prompt for an image`
2. `set theImageFile to choose file of type "public.image" with prompt ""`
4. `-- Prompt for a color`
5. `set theColor to choose color`
7. `-- Locate an output folder`
8. `set theOutputFolder to (path to desktop folder as string)`
10. `-- Launch Image Events`
11. `tell application "Image Events"`
12. `launch`
14. `-- Open the image`
15. `set theImage to open theImageFile`
16. `tell theImage`
18. `-- Determine a save name for the image`
19. `set theName to name`
20. `set theSaveName to "temp-" & theName`
22. `-- Get the current dimensions of the image`
23. `set {theWidth, theHeight} to dimensions`
25. `-- Pad the image by 20 pixels on all sides`
26. `pad to dimensions {theWidth + 20, theHeight + 20} with pad color theColor`
28. `-- Save the image to the output folder, using the save name`
29. `save as file type in (theOutputFolder & theSaveName)`
31. `-- Close the image`
32. `close`
33. `end tell`
34. `end tell`

> [!NOTE]
> 

### Converting an Image from One Type to Another

To convert an image from one type to another, open it and save it in another format. Listing 38-8 saves a chosen image in `.jpg`, `.psd`, and `.tif` format.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=--%20Prompt%20for%20an%20image%0Aset%20theImageFile%20to%20choose%20file%20of%20type%20%22public.image%22%20with%20prompt%20%22%22%0A%0A--%20Locate%20an%20output%20folder%0Aset%20theOutputFolder%20to%20%28path%20to%20desktop%20folder%20as%20string%29%0A%0A--%20Launch%20Image%20Events%0Atell%20application%20%22Image%20Events%22%0A%20%20%20%20launch%0A%0A%20%20%20%20--%20Open%20the%20image%0A%20%20%20%20set%20theImage%20to%20open%20theImageFile%0A%20%20%20%20tell%20theImage%0A%0A%20%20%20%20%20%20%20%20--%20Save%20the%20image%20as%20a%20.jpg%0A%20%20%20%20%20%20%20%20save%20as%20JPEG%20in%20%28theOutputFolder%20%26%20%22temp-conversion-output.jpg%22%29%0A%0A%20%20%20%20%20%20%20%20--%20Save%20the%20image%20as%20a%20.psd%0A%20%20%20%20%20%20%20%20save%20as%20PSD%20in%20%28theOutputFolder%20%26%20%22temp-conversion-output.psd%22%29%0A%0A%20%20%20%20%20%20%20%20--%20Save%20the%20image%20as%20a%20.tif%0A%20%20%20%20%20%20%20%20save%20as%20TIFF%20in%20%28theOutputFolder%20%26%20%22temp-conversion-output.tif%22%29%0A%0A%20%20%20%20%20%20%20%20--%20Close%20the%20image%0A%20%20%20%20%20%20%20%20close%0A%20%20%20%20end%20tell%0Aend%20tell)

__Listing 38-8__AppleScript: Converting an image from one type to another

1. `-- Prompt for an image`
2. `set theImageFile to choose file of type "public.image" with prompt ""`
4. `-- Locate an output folder`
5. `set theOutputFolder to (path to desktop folder as string)`
7. `-- Launch Image Events`
8. `tell application "Image Events"`
9. `launch`
11. `-- Open the image`
12. `set theImage to open theImageFile`
13. `tell theImage`
15. `-- Save the image as a .jpg`
16. `save as JPEG in (theOutputFolder & "temp-conversion-output.jpg")`
18. `-- Save the image as a .psd`
19. `save as PSD in (theOutputFolder & "temp-conversion-output.psd")`
21. `-- Save the image as a .tif`
22. `save as TIFF in (theOutputFolder & "temp-conversion-output.tif")`
24. `-- Close the image`
25. `close`
26. `end tell`
27. `end tell`

[Automating the User Interface](AutomatetheUserInterface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnrzfvjvomi)

[Calling Command-Line Tools](CallCommandLineUtilities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnbtfvjvomi)
