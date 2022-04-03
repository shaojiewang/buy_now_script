[TOC]
# buy_now_script
This scripts aims to buy things from taobao/JD web page and android APPs

## overview
|device |vandors| support
|--|-------- | -----
|web|taobao  | yes
|   |JD | No
|android device|taobao  | No
|  |JD|No

or HTML table like:
<table>
    <tr>
	    <th>device</th>
	    <th>vandor</th>
	    <th>support</th>  
	</tr >
    <tr>
        <td rowspan="2">chrome</td>
        <td>Taobao</td>
        <td>YES</td>
    </tr>
    <tr>
        <td>JD</td>
        <td>NO</td>
    </tr>
    <tr>
        <td rowspan="2">msEdge</td>
        <td>Taobao</td>
        <td>YES</td>
    </tr>
    <tr>
        <td>JD</td>
        <td>NO</td>
    </tr>
    <tr>
        <td rowspan="2">android</td>
        <td>Taobao</td>
        <td>NO</td>
    </tr>
    <tr>
        <td>JD</td>
        <td>NO</td>
    </tr>
</table>

## Buy things from website
**To Prepare**: You need to add all that you want to buy into your carts.
### Chrome
You need download the chromeDriver.exe on your laptop. And make sure the path of exe is in the system PATH.
#### Taobao
And then run 
```shell
python3 buy_now_test.py
```
You can change code to adjust the buying time.
#### JD
coming soon. emm maybe not so soon
### MsEdge
You can use following code to download a MsEdgeDriver.exe
```
b_op = browser_operations()
b_op.download_driver()
```
Please note that driver version may be obselete. You can change the site to get the proper driver.
#### Taobao
You can directly run:
```
python3 browser_op.py
```
even without download driver by yourself.
#### JD
coming not soon
## Buy things from android 
I'm working on intalling adb.... Sorry
