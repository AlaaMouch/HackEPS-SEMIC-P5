31627.6600
46370.1000
99189.0400
18199.5700
54638.9100
15288.6700
32748.1800
31734.6100
63720.4200
17475.6500
24965.1300
48088.9800
4594.2400
36181.3900
14489.8800
35751.2200
33282.4100
13960.1500
21619.1700
11552.7900
58728.3700
37948.8700
86451.3300
52210.6300
44746.4600
6852.4100
21045.9800
103812.6900
6417.6200
6627.0100
18062.6500
41005.7200
8937.8500
34665.1000
1848.6700
25745.6400
28790.2000
39831.9600
62395.0500
58569.6300
32837.2300
6073.3100
25816.5500
40007.3500
19463.6100
54574.6300


select sum( (ROUND(ROUND(bi.price *(1 -(bi.disount_1/100)),2)*(1-(bi.discount_2/100)),2))*bi.units) from billitems bi;
select bi.bill_id, sum(bi.price*(1-((bi.discount_1+bi.discount_2)/100))*bi.units) from billitems bi group by bill_id;
select sum(ROUND(tb.price_bill*(1-((b.soonpayment)/100))*(1-((b.discount)/100)),2)) from bills b, testbills tb where tb.bill_id = b.bill_id;
select sum(TRUNCATE(TRUNCATE(tb.price_bill*(1-((b.soonpayment)/100)),2)*(1-((b.discount)/100)),2)) from bills b, testbills tb where tb.bill_id = b.bill_id;
