---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Appendix/EditDatePopup.java.html
archived_at: '2026-07-15T08:12:21.940458Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](EditDatePopup.wod.md)

## EditDatePopup.java

```
import com.webobjects.foundation.*;
import com.webobjects.appserver.*;
import com.webobjects.eocontrol.*;
import com.webobjects.eoaccess.*;

public class EditDatePopup extends WOComponent {
    protected String day;
    protected String month;
    protected String year;
    protected EOEnterpriseObject object;
    protected String key;
    protected NSMutableArray yearList;
    protected NSMutableArray monthList;
    protected NSMutableArray dayList;
    protected static final NSTimestampFormatter DAY_FORMAT =
        new NSTimestampFormatter("%d");
    protected static final NSTimestampFormatter MONTH_FORMAT =
        new NSTimestampFormatter("%b");
    protected static final NSTimestampFormatter YEAR_FORMAT =
        new NSTimestampFormatter("%Y");
    protected static final NSTimestampFormatter ALL_FORMAT =
        new NSTimestampFormatter("%d %b %Y");

    public EditDatePopup(WOContext aContext) {
        super(aContext);
    }

    public void takeValuesFromRequest (WORequest request, WOContext context)
        throws NSValidation.Exception {
        super.takeValuesFromRequest (request,context);
        try {
            object.takeValueForKey(ALL_FORMAT.parseObject
                (day+" "+month+" "+year),key);
        } catch (Exception exception) {
            throw (new NSValidation.Exception("Date out of Range"));
        }
    }

    public NSArray yearList() {
        if (yearList == null) {
            yearList = new NSMutableArray();
            for (int year = 1950; year < 2050; year++)
                yearList.addObject(""+year);
        }
        return yearList;
    }

    public NSArray dayList() {
        if (dayList == null) {
            dayList = new NSMutableArray(new Object[] {
                "01","02","03","04","05","06","07","08","09","10",
                "11","12","13","14","15","16","17","18","19","20",
                "21","22","23","24","25","26","27","28","29","30","31"
            });
        }
        return dayList;
    }

    public NSArray monthList() {
        if (monthList == null) {
            monthList = new NSMutableArray(new Object[] {
                "Jan","Feb","Mar","Apr","May","Jun",
                "Jul","Aug","Sep","Oct","Nov","Dec"
            });
        }
        return monthList;
    }

    public String day() throws Exception {
        day = DAY_FORMAT.format(object.valueForKey(key));
    }

    public void setDay(String newDay) throws Exception {
        day = newDay;
    }

    public String month() throws Exception {
        month = MONTH_FORMAT.format(object.valueForKey(key));
        return month;
    }

    public void setMonth(String newMonth) throws Exception {
        month = newMonth;
    }

    public String year() throws Exception {
        year = YEAR_FORMAT.format(object.valueForKey(key));
        return year;
    }

    public void setYear(String newYear) throws Exception {
        year = newYear;
    }
}
```

[![Previous](attachments/DirectToWeb/Images/previous.gif)](EditDatePopup.wod.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
