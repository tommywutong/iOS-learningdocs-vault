---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Protocols/EditRelationshipPageInterf.html
archived_at: '2026-07-15T08:11:31.274585Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

[[Table of Contents]](../DirectToWebTOC.md)

# EditRelationshipPageInterface

> **__Implemented by:__**
> : [D2WEditRelationshipPage](D2WEditRelationshipPage.md)

> **__Package:__**
> : com.apple.yellow.directtoweb

---

## Interface Description

---

This interface is the return value for the D2W `editRelationshipPageForEntityNamed` method that creates an edit-relationship page. The methods defined by this interface initialize the newly created page.

## Method Types

---

> **Managing the Next Page Parameters**
> : [setNextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rlenf2fezlmmf2gs33oonugs4cqmftwksloorsxeztbmnss643forhgk6dukbqwozjpozxwszbpfblu6q3pnvyg63tfnz2cs)
> : [setNextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rlenf2fezlmmf2gs33oonugs4cqmftwksloorsxeztbmnss643forhgk6dukbqwozkemvwgkz3borss65tpnfsc6kcomv4hiudbm5suizlmmvtwc5dffe)

> **Setting the Object**
> : [setMasterObjectAndRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rlenf2fezlmmf2gs33oonugs4cqmftwksloorsxeztbmnss643forgwc43umvze6ytkmvrxiqlomrjgk3dboruw63ttnbuxas3fpexxm33jmqxsqrkpivxhizlsobzgs43fj5rguzldoqwfg5dsnfxgoki)

## Methods

---

### setMasterObjectAndRelationshipKey

abstract public void setMasterObjectAndRelationshipKey(EOEnterpriseObject anObject, String key)

Sets the object whose relationship is edited to `anObject`. Sets the property key for the relationship that is edited to `key`. For example, to edit a movie's `toStudio` relationship, set `anObject` to a Movie object and set `key to "toStudio".

---

### setNextPage

public abstract void setNextPage(WOComponent nextPage)

Sets the page that is displayed when the user clicks Return in the edit-relationship page. If the new page needs to be initialized, set the next page delegate instead.

---

### setNextPageDelegate

public abstract void setNextPageDelegate(NextPageDelegate nextPageDelegate)

Sets the receiver's next page delegate to nextPageDelegate. When the user clicks Return in the edit-relationship page, Direct to Web invokes the nextPage method on the next page delegate.

See Also:
[NextPageDelegate](NextPageDelegate.md)

---

[[Table of Contents]](../DirectToWebTOC.md)`
