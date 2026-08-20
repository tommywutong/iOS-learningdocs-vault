---
title: Creator Changer
apple_id: DTS10000216
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/Creator_Changer/Listings/Creator_Changer_Project_Source_ImageComponent_java.html
archived_at: '2026-07-18T03:05:15.620852Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Creator Changer](Creator%20Changer.md)


[Next](Creator%20Changer%20Project-Source-ProgressBar.java.md)[Previous](Creator%20Changer%20Project-Source-DefaultBorder.java.md)

# Creator Changer Project/Source/ImageComponent.java

```
import java.awt.Dimension;
import java.awt.Component;
import java.awt.Image;
import java.awt.Graphics;

/**
 * ImageComponent
 *
 * @author Levi Brown
 * @version 1.0 11/2/98
 */
public class ImageComponent extends Component
{
    /**
     * Constructs a default ImageComponent.
     */
    public ImageComponent()
    {
        image = null;
    }

    /**
     * Returns the image being displayed.
     */
    public Image getImage()
    {
        return image;
    }

    /**
     * Sets the image being displayed.
     */
    public void setImage(Image image)
    {
        this.image = image;
        repaint();
    }

    /**
     * Paints this component using the given graphics context.
     * This is a standard Java AWT method which typically gets called
     * by the AWT to handle painting this component. It paints this component
     * using the given graphics context. The graphics context clipping region
     * is set to the bounding rectangle of this component and its [0,0]
     * coordinate is this component's top-left corner.
     *
     * @param g the graphics context used for painting
     * @see java.awt.Component#repaint
     * @see java.awt.Component#update
     */
    public void paint(Graphics g)
    {
        if (image != null)
        {
            g.drawImage(image, 0, 0, this);
        }
    }

    /** 
     * Returns the preferred size of this component.
     * @see java.awt.Component#getMinimumSize
     * @see LayoutManager
     */
    public Dimension getPreferredSize()
    {
        if (image == null)
            return super.getPreferredSize();
        else
            return new Dimension(image.getWidth(this), image.getHeight(this));
    }

    protected Image image;
}
```

[Next](Creator%20Changer%20Project-Source-ProgressBar.java.md)[Previous](Creator%20Changer%20Project-Source-DefaultBorder.java.md)

