<node>
  <interface name="org.freedesktop.DBus.Introspectable">
    <method name="Introspect">
      <arg direction="out" name="data" type="s">
    </arg></method>
  <interface name="org.freedesktop.DBus.Properties">
    <method name="Get">
      <arg direction="in" name="interface" type="s">
      <arg direction="in" name="propname" type="s">
      <arg direction="out" name="value" type="v">
    </arg></arg></arg></method>
    <method name="Set">
      <arg direction="in" name="interface" type="s">
      <arg direction="in" name="propname" type="s">
      <arg direction="in" name="value" type="v">
    </arg></arg></arg></method>
    <method name="GetAll">
      <arg direction="in" name="interface" type="s">
      <arg direction="out" name="props" type="a{sv}">
    </arg></arg></method>
  </interface>
  <interface name="org.freedesktop.NetworkManager">
    <method name="state">
      <arg direction="out" name="state" type="u">
    </arg></method>
    <method name="SetLogging">
      <arg direction="in" name="level" type="s">
      <arg direction="in" name="domains" type="s">
    </arg></arg></method>
    <method name="GetPermissions">
      <arg direction="out" name="permissions" type="a{ss}">
    </arg></method>
    <method name="Enable">
      <arg direction="in" name="enable" type="b">
    </arg></method>
    <method name="Sleep">
      <arg direction="in" name="sleep" type="b">
    </arg></method>
    <method name="DeactivateConnection">
      <arg direction="in" name="active_connection" type="o">
    </arg></method>
    <method name="AddAndActivateConnection">
      <arg direction="in" name="connection" type="a{sa{sv}}">
      <arg direction="in" name="device" type="o">
      <arg direction="in" name="specific_object" type="o">
      <arg direction="out" name="path" type="o">
      <arg direction="out" name="active_connection" type="o">
    </arg></arg></arg></arg></arg></method>
    <method name="ActivateConnection">
      <arg direction="in" name="connection" type="o">
      <arg direction="in" name="device" type="o">
      <arg direction="in" name="specific_object" type="o">
      <arg direction="out" name="active_connection" type="o">
    </arg></arg></arg></arg></method>
    <method name="GetDeviceByIpIface">
      <arg direction="in" name="iface" type="s">
      <arg direction="out" name="device" type="o">
    </arg></arg><<method>
    <method name="GetDevices">
      <arg direction="out" name="devices" type="ao">
    </arg></method>
     <signal name="DeviceRemoved">
       <arg type="o">
     </arg> </signal>
     <signal name="DeviceAdded">
       <arg type="o">
     </arg> </signal>
     <signal name="PropertiesChanged">
       <arg type="a{sv}">
     </arg> </signal>
     <signal name="StateChanged">
       <arg type="u">
     </arg> </signal>
     <signal name="CheckPermissions">
     </signal>
     <property access="read" name="State" type="u">
     <property access="read" name="Version" type="s">
     <property access="read" name="ActiveConnections" type="ao">
     <property access="read" name="WimaxHardwareEnabled" type="b">
     <property access="readwrite" name="WimaxEnabled" type="b">
     <property access="read" name="WwanHardwareEnabled" type="b">
     <property access="readwrite" name="WwanEnabled" type="b">
     <property access="read" name="WirelessHardwareEnabled" type="b">
     <property access="readwrite" name="WirelessEnabled" type="b">
     <property access="read" name="NetworkingEnabled" type="b">
   </property> </property> </property> </property> </property> </property> </property> </property> </property> </property>
   <node name="AccessPoint">
   <node name="ActiveConnection">
   <node name="AgentManager">
   <node name="DHCP4Config">
   <node name="Devices">
   <node name="IP4Config">
   <node name="Settings">
 </node>
" </node> </node> </node> </node> </node> </node>