---
title: SpecialPictureProtocol
apple_id: DTS10003816
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/samplecode/SpecialPictureProtocol/Listings/test_html.html
archived_at: '2026-07-18T03:25:16.072685Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpecialPictureProtocol](SpecialPictureProtocol.md)


[Next](Document%20Revision%20History.md)[Previous](SpecialProtocol.m.md)

# test.html

```
<html>
<head>
    <title>SpecialPictureProtocol Example</title>
</head>
<body>
<script type="text/javascript" language="JavaScript1.4"><!--

function NewText() {
    var textField = document.getElementById('stringtext');
    if (  textField.value != '' ) {
        var imageList = document.getElementById('image_list');
        var theNewURL = 'special:///' + escape(textField.value);
        imageList.innerHTML = '<img src="' + theNewURL + '" id="stringimage"><br>' + imageList.innerHTML;
    }
}

// -->
</script>

    <img src="special:///Example">

    <!-- we have implemented a special NSURLProtocol that uses the 'special'
    scheme to identify urls it is capable of handling.  Our protocol simply
    renders the path part of the URL into a jpeg image.  We use this scheme
    here to produce images in the html.  -->

    <form action="" method="get" onSubmit="return false;">

        <p>Type your text here:<br> 
        <input name="seconds" id="stringtext" type="text" size="21" onKeyUp="NewText();" value="Special Example"></p>
        <p>Images will appear below as you type:</p>
        <div id="image_list">
            <img src="special:///Special%20Example" id="stringimage">
        </div>
    </form> 

<script type="text/javascript" language="JavaScript1.4"><!--

    document.getElementById('stringtext').select();

// -->
</script>

</body>
</html>
```

[Next](Document%20Revision%20History.md)[Previous](SpecialProtocol.m.md)

