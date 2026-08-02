---
title: WebObjects Direct to Web Guide
apple_id: TP30001015
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-07-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_With_D2W/Appendix/Appendix.html
archived_at: '2026-07-18T02:20:18.883043Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Direct to Web Guide](Introduction%20to%20WebObjects%20Direct%20to%20Web%20Guide.md)


[Previous](Customizing%20a%20Direct%20to%20Web%20Application.md)

# EditStatePopup Listings

The EditStatePopup.wo property-level component is listed here. The component has an HTML template (`.html`) file, a bindings (`.wod`) file, and a source (`.java`) file.


```
<WEBOBJECTNAME=PopUpButton1></WEBOBJECT>
```



```
PopUpButton1:WOPopUpButton {
    list = stateList;
    selection = state;
}
```



```

import com.webobjects.foundation.*;
import com.webobjects.appserver.*;
import com.webobjects.eocontrol.*;
import com.webobjects.eoaccess.*;

public class EditStatePopupextends WOComponent {
    protected String state;
    protected EOEnterpriseObjectobject;
    protected String key;
    protected NSMutableArraystateList;

    public EditStatePopup(WOContextcontext) {
        super(context);
    }

    public void takeValuesFromRequest(WORequest request, WOContext context)
        throws NSValidation.ValidationException{
        super.takeValuesFromRequest(request,context);
        try {
            object.takeValueForKey(state,key);
        } catch (Exception exception){
            throw (new NSValidation.ValidationException(“Incorrectstate
                    input”));
        }
    }

    public NSArray stateList(){
        if (stateList == null){
            stateList = newNSMutableArray(new Object[] {
                "AL","AK", "AZ", "AR", "CA","CO", "CT", "DE", "FL","GA",
                "HI","ID", "IL", "IN", "IA","KS", "KY", "LA", "ME","MD",
                "MA","MI", "MN", "MS", "MO","MT", "NE", "NV", "NH","NJ",
                "NM","NY", "NC", "ND", "OH","OK", "OR", "PA", "RI","SC",
                "SD","TN", "TX", "UT", "VT","VA", "WA", "WV", "WI","WY"
            });
        }
        return stateList;
    }

    public String state() throwsException {
        state = (String)object.valueForKey(key);
        return state;
    }

    public void setState(StringnewState) throws Exception {
        state = newState;
    }
}
```

[Previous](Customizing%20a%20Direct%20to%20Web%20Application.md)

