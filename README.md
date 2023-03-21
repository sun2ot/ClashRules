> 如 emoji 显示异常，如不显示、与目标国家不符等，请提交 issue

## 部分规则来源

1. [Semporia：Clash](https://github.com/Semporia/Clash)

2. [Loyalsoldier：clash-rules](https://github.com/Loyalsoldier/clash-rules)

3. [ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)


## 使用方法

### 方法1. 手动修改配置文件

将最下方的 `rules` 和 `rule-providers` 复制粘贴/替换 到 Clash 的配置文件中

### 方法2. 自建 subconverter 

1. 本地部署/线上部署 `subconverter`，见[github·subconverter](https://github.com/tindy2013/subconverter/blob/master/README-cn.md)
2. 复制仓库中的 `config/test.ini` 文件到 `subconverter` 根路径下的 `config/` 目录中
4. `all_base.tpl` 同理，建议阅读 `subconverter` 文档后**自行决定是否替换**
5. 修改 `subconverter` 根路径下的 `pref.toml` ，将 `api_access_token` 改为如下所示
```toml
api_access_token = "随便设个密码"
```
6. 在 `subconverter` 根路径下的 `profiles/` 目录下(没有这个目录就建一个)，新建 `任意名称.ini` 文件，内容如下
```ini
target=clash
new_name=true
url=订阅链接
clash.dns=1   // 如果没有替换 `all_base.tpl`，就不要加这一行！！！
config=config/test.ini
exclude=(套餐|官网|频道)
filename=任意名称
expand=false
```
7. 通过 `subconverter` 订阅即可，订阅链接为 `http(s)://你的ip(:25500)/getprofile?name=profiles/任意名称.ini&token=你设置的密码`

### 方法3. 利用现成的订阅转换网站，远程引用配置文件

1. 在订阅转换网站的页面中，会有一个下拉菜单让你选择**远程配置**，此处填写 `https://raw.githubusercontent.com/sun2ot/ClashRules/main/config/test.ini`
> Tips: 配置文件中已经嵌入了 emoji 配置
2. 推荐在生成的订阅链接末尾加上参数 `&expand=false`
3. 其他更多参数见 `subconverter` [官方文档](https://github.com/tindy2013/subconverter/blob/master/README-cn.md#%E8%B0%83%E7%94%A8%E8%AF%B4%E6%98%8E-%E8%BF%9B%E9%98%B6)


```yaml
rules:
  - RULE-SET,SteamCN,🎮️ Steam
  - RULE-SET,Steam,🎮️ Steam
  - RULE-SET,Bahamut,📺️ 动画疯
  - RULE-SET,BilibiliHMT,🅱 Bilibili
  - RULE-SET,Microsoft,Ⓜ️ Microsoft
  - RULE-SET,Weibo,👊 微博
  - RULE-SET,GoogleVoice,📞 GoogleVoice
  - RULE-SET,CustomizeDirect,🎯 全球直连
  - RULE-SET,CustomizeProxy,🚀 节点选择
  - RULE-SET,CustomizeReject,🛑 拦截
  - RULE-SET,telegramcidr,🚀 节点选择
  - RULE-SET,proxy,🚀 节点选择
  - RULE-SET,cncidr,🎯 全球直连
  - RULE-SET,direct,🎯 全球直连
  - RULE-SET,reject,🛑 拦截
  - MATCH,🐟 漏网之鱼
rule-providers:
  SteamCN:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/SteamCN.yaml
    path: ./providers/rule-provider_SteamCN.yaml
    interval: 86400
  Steam:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Steam.yaml
    path: ./providers/rule-provider_Steam.yaml
    interval: 86400
  Bahamut:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Bahamut.yaml
    path: ./providers/rule-provider_Bahamut.yaml
    interval: 86400
  BilibiliHMT:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/sun2ot/ClashRules/main/RuleSet/BilibiliHMT.yaml
    path: ./providers/rule-provider_BilibiliHMT.yaml
    interval: 86400
  Microsoft:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/Semporia/Clash/master/Rule/Microsoft.yaml
    path: ./providers/rule-provider_Microsoft.yaml
    interval: 86400
  Weibo:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/sun2ot/ClashRules/main/RuleSet/Weibo.yaml
    path: ./providers/rule-provider_Weibo.yaml
    interval: 86400
  GoogleVoice:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleVoice/GoogleVoice.yaml
    path: ./providers/rule-provider_GoogleVoice.yaml
    interval: 86400
  CustomizeDirect:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/sun2ot/ClashRules/main/RuleSet/CustomizeDirect.yaml
    path: ./providers/rule-provider_CustomizeDirect.yaml
    interval: 86400
  CustomizeProxy:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/sun2ot/ClashRules/main/RuleSet/CustomizeProxy.yaml
    path: ./providers/rule-provider_CustomizeProxy.yaml
    interval: 86400
  CustomizeReject:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/sun2ot/ClashRules/main/RuleSet/CustomizeReject.yaml
    path: ./providers/rule-provider_CustomizeReject.yaml
    interval: 86400
  telegramcidr:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/telegramcidr.txt
    path: ./providers/rule-provider_telegramcidr.yaml
    interval: 86400
  proxy:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt
    path: ./providers/rule-provider_proxy.yaml
    interval: 86400
  cncidr:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/cncidr.txt
    path: ./providers/rule-provider_cncidr.yaml
    interval: 86400
  direct:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/direct.txt
    path: ./providers/rule-provider_direct.yaml
    interval: 86400
  reject:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/reject.txt
    path: ./providers/rule-provider_reject.yaml
    interval: 86400
```
