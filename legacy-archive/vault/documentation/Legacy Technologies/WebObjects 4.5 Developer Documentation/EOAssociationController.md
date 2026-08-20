---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOAssociationController.html
archived_at: '2026-07-15T08:11:43.652520Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EOAssociationController

> **__Inherits
> from:__**
> : [EOWidgetController](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOWidgetController.html#//apple_ref/java/cl/EOWidgetController) :
> EOComponentController (eoapplication) :
> EOController (eoapplication) :
> Object

> **__Implements:__**
> : EOEditable
> : (eoapplication package)
> : EOAssociationConnector (eoapplication package)

> **__Package:__**
> : com.apple.client.eogeneration

---

## Class Description

---

Documentation for this class is forthcoming.
For information on using this class, see the book _Getting Started
with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| None (abstract class) | `widgetController` |

## Method Types

---

> **All methods**
> : [EOAssociationController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixukt2bonzw6y3jmf2gs33oinxw45dsn5wgyzls)
> : [association](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwc43tn5rwsylunfxw4)
> : [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwg33onzswg5djn5xfoyltijzg623fny)
> : [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwg33onzswg5djn5xfoyltivzxiylcnruxg2dfmq)
> : [controllerDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwg33oorzg63dmmvzei2ltobwgc6khojxxk4a)
> : [displayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwi2ltobwgc6khojxxk4a)
> : [displayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwi2ltobwgc6khojxxk4cqojxxm2lemvze2zlunbxwittbnvsq)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwi2ltobxxgzi)
> : [disposeAssociations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwi2ltobxxgzkbonzw6y3jmf2gs33oom)
> : [disposeIfTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwi2ltobxxgzkjmzkheyloonuwk3tu)
> : [editability](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwkzdjorqwe2lmnf2hs)
> : [enabledDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwk3tbmjwgkzcenfzxa3dbpfdxe33voa)
> : [enabledDisplayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwk3tbmjwgkzcenfzxa3dbpfdxe33vobihe33wnfsgk4snmv2gq33ejzqw2zi)
> : [enabledKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixwk3tbmjwgkzclmv4q)
> : [isEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixws42fmruxiylcnrsq)
> : [newAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixw4zlxifzxg33dnfqxi2lpny)
> : [setAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxgzluifzxg33dnfqxi2lpny)
> : [setDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxgzluiruxg4dmmf4uo4tpovya)
> : [setDisplayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxgzluiruxg4dmmf4uo4tpovyfa4tpozuwizlsjvsxi2dpmrhgc3lf)
> : [setEditability](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxgzluivsgs5dbmjuwy2lupe)
> : [setEnabledDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxgzluivxgcytmmvsei2ltobwgc6khojxxk4a)
> : [setEnabledDisplayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxgzluivxgcytmmvsei2ltobwgc6khojxxk4cqojxxm2lemvze2zlunbxwittbnvsq)
> : [setEnabledKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxgzluivxgcytmmvsewzlz)
> : [supercontrollerEditabilityDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxg5lqmvzgg33oorzg63dmmvzekzdjorqwe2lmnf2hsrdjmrbwqylom5sq)
> : [takeResposibilityForConnectionOfAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxiyllmvjgk43qn5zwsytjnruxi6kgn5zeg33onzswg5djn5xe6zsbonzw6y3jmf2gs33o)
> : [takeResposibilityForEditabilityOfAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxiyllmvjgk43qn5zwsytjnruxi6kgn5zekzdjorqwe2lmnf2hst3gifzxg33dnfqxi2lpny)
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnzbw63tuojxwy3dfoixxi32torzgs3th)

## Constructors

---

### EOAssociationController

`public EOAssociationController(
com.apple.client.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### association

`public com.apple.client.eointerface.EOAssociation association()`

---

### connectionWasBroken

`protected void connectionWasBroken()`

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

---

### controllerDisplayGroup

`public com.apple.client.eointerface.EODisplayGroup controllerDisplayGroup()`

---

### displayGroup

`public com.apple.client.eointerface.EODisplayGroup displayGroup()`

---

### displayGroupProviderMethodName

`public String displayGroupProviderMethodName()`

---

### dispose

`public void dispose()`

---

### disposeAssociations

`protected void disposeAssociations()`

---

### disposeIfTransient

`protected boolean disposeIfTransient()`

---

### editability

`public int editability()`

---

### enabledDisplayGroup

`public com.apple.client.eointerface.EODisplayGroup enabledDisplayGroup()`

---

### enabledDisplayGroupProviderMethodName

`public String enabledDisplayGroupProviderMethodName()`

---

### enabledKey

`public String enabledKey()`

---

### isEditable

`public boolean isEditable()`

---

### newAssociation

`protected abstract com.apple.client.eointerface.EOAssociation newAssociation(
javax.swing.JComponent aJComponent,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup,
String aString,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### setAssociation

`public void setAssociation(com.apple.client.eointerface.EOAssociation anEOAssociation)`

---

### setDisplayGroup

`public void setDisplayGroup(com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### setDisplayGroupProviderMethodName

`public void setDisplayGroupProviderMethodName(String aString)`

---

### setEditability

`public void setEditability(int anInt)`

---

### setEnabledDisplayGroup

`public void setEnabledDisplayGroup(com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### setEnabledDisplayGroupProviderMethodName

`public void setEnabledDisplayGroupProviderMethodName(String aString)`

---

### setEnabledKey

`public void setEnabledKey(String aString)`

---

### supercontrollerEditabilityDidChange

`public void supercontrollerEditabilityDidChange()`

---

### takeResposibilityForConnectionOfAssociation

`public void takeResposibilityForConnectionOfAssociation(com.apple.client.eointerface.EOAssociation anEOAssociation)`

---

### takeResposibilityForEditabilityOfAssociation

`public void takeResposibilityForEditabilityOfAssociation(com.apple.client.eointerface.EOAssociation anEOAssociation)`

---

### toString

`public String toString()`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
