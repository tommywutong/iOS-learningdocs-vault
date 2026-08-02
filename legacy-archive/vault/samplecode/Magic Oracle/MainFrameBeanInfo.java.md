---
title: Magic Oracle
apple_id: DTS10000220
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/Magic_Oracle/Listings/MainFrameBeanInfo_java.html
archived_at: '2026-07-18T03:14:09.961242Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Magic Oracle](Magic%20Oracle.md)


[Next](Util.java.md)[Previous](MainFrame.java.md)

# MainFrameBeanInfo.java

```
import java.beans.*;
import java.lang.reflect.*;

public class MainFrameBeanInfo extends SimpleBeanInfo 
{
    /**
     * A method descriptor used by AppleScript for Java's introspector to generate the aete
     * This descriptor describes the parameters and method to be published in the aete and
     * overrides the default generated values
     */
    public MethodDescriptor[] getMethodDescriptors()    
    {
        MethodDescriptor md[] = new MethodDescriptor[1];    // the method descriptor provides 
                                                            // extra information to the introspector
        try
        {
            /** Creating a parameter descriptor allows you to specify a formal name in the terminology
              * for the paramter(s) of a method. In this instance, you will be able to write:
              *
              * ask Oracle of <object> question "Whatever"
              * 
              * instead of:
              * 
              *  ask Oracle of <object> parameters { "Whatever" }
              * 
              */

            ParameterDescriptor[] pd = new ParameterDescriptor[1];
            pd[0] = new ParameterDescriptor();
            pd[0].setShortDescription( "Question to ask of the oracle." );
            pd[0].setName( "question" );

            md[0] = new MethodDescriptor( getMethod( MainFrame.class, "askMystic" ), pd) ;
            md[0].setShortDescription( "Ask the Oracle a yes/no question and receive a response." );

            return md;
        }
        catch ( IntrospectionException e )
        {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * getMethod is called by the introspector to return a list of methods in the class
     */
    Method getMethod( Class c, String methodName )  throws IntrospectionException
    {
        Method methods[] = c.getMethods();

        for ( int i = 0; i < methods.length; i++ )
        {
            if ( methods[i].getName().equals( methodName )) 
            {
                return methods[i];
            }
        }
        throw new IntrospectionException( "No such method \"" + methodName + "\"" );
    }



}
```

[Next](Util.java.md)[Previous](MainFrame.java.md)

