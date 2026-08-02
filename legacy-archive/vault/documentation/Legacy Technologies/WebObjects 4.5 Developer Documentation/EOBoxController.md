---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOBoxController.html
archived_at: '2026-07-15T08:11:36.313695Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOBoxController

> **__Inherits
> from:__**
> : [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi) : [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza) : Object

> **__Package:__**
> : com.apple.client.eoapplication

---

## Class Description

---

Documentation for this class is forthcoming.
For information on using this class, see the book _Getting Started
with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `BOXCONTROLLER` | `groupingController` |

## Method Types

---

> **All methods**
> : [EOBoxController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel2fj5bg66cdn5xhi4tpnrwgk4q)
> : [borderType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3cn5zgizlskr4xazi)
> : [generateComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3hmvxgk4tborsug33nobxw4zlooq)
> : [highlightsTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3inftwq3djm5uhi42unf2gyzi)
> : [horizontalBorder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3in5zgs6tpnz2gc3ccn5zgizls)
> : [setBorderType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3tmv2ee33smrsxevdzobsq)
> : [setHighlightsTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3tmv2eq2lhnbwgsz3iorzvi2lunrsq)
> : [setHorizontalBorder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3tmv2eq33snf5g63tumfwee33smrsxe)
> : [setTitleColor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3tmv2fi2lunrsug33mn5za)
> : [setTitleFont](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3tmv2fi2lunrsum33ooq)
> : [setTitlePosition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3tmv2fi2lunrsva33tnf2gs33o)
> : [setUsesTitledBorder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3tmv2fk43fonkgs5dmmvsee33smrsxe)
> : [setVerticalBorder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3tmv2fmzlsoruwgylmijxxezdfoi)
> : [titleColor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3unf2gyzkdn5wg64q)
> : [titleFont](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3unf2gyzkgn5xhi)
> : [titlePosition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3unf2gyzkqn5zws5djn5xa)
> : [usesTitledBorder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3vonsxgvdjorwgkzccn5zgizls)
> : [verticalBorder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpijxxqq3pnz2he33mnrsxel3wmvzhi2ldmfwee33smrsxe)

## Constructors

---

### EOBoxController

`public EOBoxController(EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### borderType

`public int borderType()`

---

### generateComponent

`protected void generateComponent()`

---

### highlightsTitle

`public boolean highlightsTitle()`

---

### horizontalBorder

`public int horizontalBorder()`

---

### setBorderType

`public void setBorderType(int anInt)`

---

### setHighlightsTitle

`public void setHighlightsTitle(boolean aBoolean)`

---

### setHorizontalBorder

`public void setHorizontalBorder(int anInt)`

---

### setTitleColor

`public void setTitleColor(java.awt.Color aColor)`

---

### setTitleFont

`public void setTitleFont(java.awt.Font aFont)`

---

### setTitlePosition

`public void setTitlePosition(int anInt)`

---

### setUsesTitledBorder

`public void setUsesTitledBorder(boolean aBoolean)`

---

### setVerticalBorder

`public void setVerticalBorder(int anInt)`

---

### titleColor

`public java.awt.Color titleColor()`

---

### titleFont

`public java.awt.Font titleFont()`

---

### titlePosition

`public int titlePosition()`

---

### usesTitledBorder

`public boolean usesTitledBorder()`

---

### verticalBorder

`public int verticalBorder()`

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
