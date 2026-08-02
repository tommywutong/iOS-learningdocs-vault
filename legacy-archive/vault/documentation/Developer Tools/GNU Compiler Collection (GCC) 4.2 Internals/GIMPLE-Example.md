---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/GIMPLE-Example.html
archived_at: '2026-07-15T07:31:01.991114Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Rough GIMPLE Grammar](Rough-GIMPLE-Grammar.md#apple-kjxxkz3ifvdustkqjrcs2r3smfww2yls),
Previous: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt),
Up: [GIMPLE](GIMPLE.md#apple-i5eu2ucmiu)

---

#### 10.2.5 GIMPLE Example


```
     struct A { A(); ~A(); };

     int i;
     int g();
     void f()
     {
       A a;
       int j = (--i, i ? 0 : 1);

       for (int x = 42; x > 0; --x)
         {
           i += g()*4 + 32;
         }
     }
```

becomes

```
     void f()
     {
       int i.0;
       int T.1;
       int iftmp.2;
       int T.3;
       int T.4;
       int T.5;
       int T.6;

       {
         struct A a;
         int j;

         __comp_ctor (&a);
         try
           {
             i.0 = i;
             T.1 = i.0 - 1;
             i = T.1;
             i.0 = i;
             if (i.0 == 0)
               iftmp.2 = 1;
             else
               iftmp.2 = 0;
             j = iftmp.2;
             {
               int x;

               x = 42;
               goto test;
               loop:;

               T.3 = g ();
               T.4 = T.3 * 4;
               i.0 = i;
               T.5 = T.4 + i.0;
               T.6 = T.5 + 32;
               i = T.6;
               x = x - 1;

               test:;
               if (x > 0)
                 goto loop;
               else
                 goto break_;
               break_:;
             }
           }
         finally
           {
             __comp_dtor (&a);
           }
       }
     }
```
