from bs4 import BeautifulSoup
import cssutils
cssutils.log.setLevel("ERROR")


def svg_css_to_inline(svg_code):
    soup = BeautifulSoup(svg_code, "xml")

    # 提取并解析 style 标签里的 CSS
    style_tag = soup.find("style")
    if not style_tag:
        return "\n".join(str(soup).splitlines()[1:])

    css_text = style_tag.string
    sheet = cssutils.parseString(css_text)

    # 遍历每条 CSS 规则
    for rule in sheet:
        if rule.type != rule.STYLE_RULE:
            continue

        selector = rule.selectorText
        style_dict = {}
        for prop in rule.style:
            style_dict[prop.name] = prop.value

        # 根据选择器找到对应元素并写入内联样式
        # 注意：BeautifulSoup 的 select 支持大部分 CSS 选择器
        elements = soup.select(selector)
        for elem in elements:
            existing_style = str(elem.get("style", ""))
            # 合并已有样式和新样式
            new_style = existing_style
            for k, v in style_dict.items():
                if k not in new_style:
                    new_style += f"{k}:{v};"
            elem["style"] = new_style

    # 删除 style 标签
    style_tag.decompose()

    return "\n".join(str(soup).splitlines()[1:])


# 使用示例
svg_code = """    <svg
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      id="chart-3d64d72c-2d16-4fdc-a297-7c6382a11dfc"
      class="pygal-chart"
      viewBox="0 0 700 2000"
    >
      <!--Generated with pygal 3.1.0 (lxml) ©Kozea 2012-2025 on 2026-05-28--><!--http://pygal.org--><!--http://github.com/Kozea/pygal-->
      <defs>
        <style type="text/css">
          .pygal-chart{-webkit-user-select:none;-webkit-font-smoothing:antialiased;font-family:"Alibaba PuHuiTi","阿里巴巴普惠体",-apple-system,sans-serif}.pygal-chart .title{font-family:"Alibaba PuHuiTi","阿里巴巴普惠体",-apple-system,sans-serif;font-size:30px}.pygal-chart .legends .legend text{font-family:"Alibaba PuHuiTi","阿里巴巴普惠体",-apple-system,sans-serif;font-size:14px}.pygal-chart .axis text{font-family:"Alibaba PuHuiTi","阿里巴巴普惠体",-apple-system,sans-serif;font-size:18px}.pygal-chart .axis text.major{font-family:"Alibaba PuHuiTi","阿里巴巴普惠体",-apple-system,sans-serif;font-size:18px}.pygal-chart .text-overlay text.value{font-family:"Alibaba PuHuiTi","阿里巴巴普惠体",-apple-system,sans-serif;font-size:16px}.pygal-chart .text-overlay text.label{font-family:"Alibaba PuHuiTi","阿里巴巴普惠体",-apple-system,sans-serif;font-size:10px}.pygal-chart .tooltip{font-family:"Alibaba PuHuiTi","阿里巴巴普惠体",-apple-system,sans-serif;font-size:14px}.pygal-chart text.no_data{font-family:"Alibaba PuHuiTi","阿里巴巴普惠体",-apple-system,sans-serif;font-size:64px}
          .pygal-chart{background-color:rgba(249,249,249,1)}.pygal-chart path,.pygal-chart line,.pygal-chart rect,.pygal-chart circle{-webkit-transition:150ms;-moz-transition:150ms;transition:150ms}.pygal-chart .graph &gt; .background{fill:rgba(249,249,249,1)}.pygal-chart .plot &gt; .background{fill:rgba(255,255,255,1)}.pygal-chart .graph{fill:rgba(0,0,0,.87)}.pygal-chart text.no_data{fill:rgba(0,0,0,1)}.pygal-chart .title{fill:rgba(0,0,0,1)}.pygal-chart .legends .legend text{fill:rgba(0,0,0,.87)}.pygal-chart .legends .legend:hover text{fill:rgba(0,0,0,1)}.pygal-chart .axis .line{stroke:rgba(0,0,0,1)}.pygal-chart .axis .guide.line{stroke:rgba(0,0,0,.54)}.pygal-chart .axis .major.line{stroke:rgba(0,0,0,.87)}.pygal-chart .axis text.major{fill:rgba(0,0,0,1)}.pygal-chart .axis.y .guides:hover .guide.line,.pygal-chart .line-graph .axis.x .guides:hover .guide.line,.pygal-chart .stackedline-graph .axis.x .guides:hover .guide.line,.pygal-chart .xy-graph .axis.x .guides:hover .guide.line{stroke:rgba(0,0,0,1)}.pygal-chart .axis .guides:hover text{fill:rgba(0,0,0,1)}.pygal-chart .reactive{fill-opacity:.7;stroke-opacity:.8;stroke-width:1}.pygal-chart .ci{stroke:rgba(0,0,0,.87)}.pygal-chart .reactive.active,.pygal-chart .active .reactive{fill-opacity:.8;stroke-opacity:.9;stroke-width:4}.pygal-chart .ci .reactive.active{stroke-width:1.5}.pygal-chart .series text{fill:rgba(0,0,0,1)}.pygal-chart .tooltip rect{fill:rgba(255,255,255,1);stroke:rgba(0,0,0,1);-webkit-transition:opacity 150ms;-moz-transition:opacity 150ms;transition:opacity 150ms}.pygal-chart .tooltip .label{fill:rgba(0,0,0,.87)}.pygal-chart .tooltip .label{fill:rgba(0,0,0,.87)}.pygal-chart .tooltip .legend{font-size:.8em;fill:rgba(0,0,0,.54)}.pygal-chart .tooltip .x_label{font-size:.6em;fill:rgba(0,0,0,1)}.pygal-chart .tooltip .xlink{font-size:.5em;text-decoration:underline}.pygal-chart .tooltip .value{font-size:1.5em}.pygal-chart .bound{font-size:.5em}.pygal-chart .max-value{font-size:.75em;fill:rgba(0,0,0,.54)}.pygal-chart .map-element{fill:rgba(255,255,255,1);stroke:rgba(0,0,0,.54) !important}.pygal-chart .map-element .reactive{fill-opacity:inherit;stroke-opacity:inherit}.pygal-chart .color-0,.pygal-chart .color-0 a:visited{stroke:#F44336;fill:#F44336}.pygal-chart .color-1,.pygal-chart .color-1 a:visited{stroke:#3F51B5;fill:#3F51B5}.pygal-chart .color-2,.pygal-chart .color-2 a:visited{stroke:#009688;fill:#009688}.pygal-chart .text-overlay .color-0 text{fill:black}.pygal-chart .text-overlay .color-1 text{fill:black}.pygal-chart .text-overlay .color-2 text{fill:black}
          .pygal-chart text.no_data{text-anchor:middle}.pygal-chart .guide.line{fill:none}.pygal-chart .centered{text-anchor:middle}.pygal-chart .title{text-anchor:middle}.pygal-chart .legends .legend text{fill-opacity:1}.pygal-chart .axis.x text{text-anchor:middle}.pygal-chart .axis.x:not(.web) text[transform]{text-anchor:start}.pygal-chart .axis.x:not(.web) text[transform].backwards{text-anchor:end}.pygal-chart .axis.y text{text-anchor:end}.pygal-chart .axis.y text[transform].backwards{text-anchor:start}.pygal-chart .axis.y2 text{text-anchor:start}.pygal-chart .axis.y2 text[transform].backwards{text-anchor:end}.pygal-chart .axis .guide.line{stroke-dasharray:4,4;stroke:black}.pygal-chart .axis .major.guide.line{stroke-dasharray:6,6;stroke:black}.pygal-chart .horizontal .axis.y .guide.line,.pygal-chart .horizontal .axis.y2 .guide.line,.pygal-chart .vertical .axis.x .guide.line{opacity:0}.pygal-chart .horizontal .axis.always_show .guide.line,.pygal-chart .vertical .axis.always_show .guide.line{opacity:1 !important}.pygal-chart .axis.y .guides:hover .guide.line,.pygal-chart .axis.y2 .guides:hover .guide.line,.pygal-chart .axis.x .guides:hover .guide.line{opacity:1}.pygal-chart .axis .guides:hover text{opacity:1}.pygal-chart .nofill{fill:none}.pygal-chart .subtle-fill{fill-opacity:.2}.pygal-chart .dot{stroke-width:1px;fill-opacity:1;stroke-opacity:1}.pygal-chart .dot.active{stroke-width:5px}.pygal-chart .dot.negative{fill:transparent}.pygal-chart text,.pygal-chart tspan{stroke:none !important}.pygal-chart .series text.active{opacity:1}.pygal-chart .tooltip rect{fill-opacity:.95;stroke-width:.5}.pygal-chart .tooltip text{fill-opacity:1}.pygal-chart .showable{visibility:hidden}.pygal-chart .showable.shown{visibility:visible}.pygal-chart .gauge-background{fill:rgba(229,229,229,1);stroke:none}.pygal-chart .bg-lines{stroke:rgba(249,249,249,1);stroke-width:2px}
        </style>
      </defs>
      <title>国内商品(2026-05-27)</title>
      <g class="graph horizontalstackedbar-graph horizontal">
        <rect x="0" y="0" width="700" height="2000" class="background" />
        <g transform="translate(94, 60)" class="plot">
          <rect x="0" y="0" width="585.2" height="1856.0" class="background" />
          <g class="axis y">
            <g class="guides">
              <text x="-5" y="1815.7258911819888" class="">jd2608</text>
              <title>0.006097560976</title>
            </g>
            <g class="guides">
              <text x="-5" y="1793.9622889305815" class="">FG609</text>
              <title>0.01829268293</title>
            </g>
            <g class="guides">
              <text x="-5" y="1772.1986866791744" class="">fb2607</text>
              <title>0.03048780488</title>
            </g>
            <g class="guides">
              <text x="-5" y="1750.4350844277674" class="">SF607</text>
              <title>0.04268292683</title>
            </g>
            <g class="guides">
              <text x="-5" y="1728.67148217636" class="">ec2606</text>
              <title>0.05487804878</title>
            </g>
            <g class="guides">
              <text x="-5" y="1706.907879924953" class="">j2609</text>
              <title>0.06707317073</title>
            </g>
            <g class="guides">
              <text x="-5" y="1685.144277673546" class="">jm2609</text>
              <title>0.07926829268</title>
            </g>
            <g class="guides">
              <text x="-5" y="1663.380675422139" class="">SM607</text>
              <title>0.09146341463</title>
            </g>
            <g class="guides">
              <text x="-5" y="1641.6170731707316" class="">a2607</text>
              <title>0.1036585366</title>
            </g>
            <g class="guides">
              <text x="-5" y="1619.8534709193245" class="">PF607</text>
              <title>0.1158536585</title>
            </g>
            <g class="guides">
              <text x="-5" y="1598.0898686679175" class="">PX607</text>
              <title>0.1280487805</title>
            </g>
            <g class="guides">
              <text x="-5" y="1576.3262664165102" class="">CJ609</text>
              <title>0.1402439024</title>
            </g>
            <g class="guides">
              <text x="-5" y="1554.5626641651031" class="">v2609</text>
              <title>0.1524390244</title>
            </g>
            <g class="guides">
              <text x="-5" y="1532.799061913696" class="">PR607</text>
              <title>0.1646341463</title>
            </g>
            <g class="guides">
              <text x="-5" y="1511.035459662289" class="">p2609</text>
              <title>0.1768292683</title>
            </g>
            <g class="guides">
              <text x="-5" y="1489.2718574108817" class="">ss2607</text>
              <title>0.1890243902</title>
            </g>
            <g class="guides">
              <text x="-5" y="1467.5082551594746" class="">TA609</text>
              <title>0.2012195122</title>
            </g>
            <g class="guides">
              <text x="-5" y="1445.7446529080676" class="">PK610</text>
              <title>0.2134146341</title>
            </g>
            <g class="guides">
              <text x="-5" y="1423.9810506566603" class="">cs2607</text>
              <title>0.2256097561</title>
            </g>
            <g class="guides">
              <text x="-5" y="1402.2174484052532" class="">SA609</text>
              <title>0.237804878</title>
            </g>
            <g class="guides">
              <text x="-5" y="1380.4538461538461" class="">OI609</text>
              <title>0.25</title>
            </g>
            <g class="guides">
              <text x="-5" y="1358.690243902439" class="">nr2607</text>
              <title>0.262195122</title>
            </g>
            <g class="guides">
              <text x="-5" y="1336.9266416510318" class="">AP610</text>
              <title>0.2743902439</title>
            </g>
            <g class="guides">
              <text x="-5" y="1315.1630393996247" class="">op2607</text>
              <title>0.2865853659</title>
            </g>
            <g class="guides">
              <text x="-5" y="1293.3994371482177" class="">lg2607</text>
              <title>0.2987804878</title>
            </g>
            <g class="guides">
              <text x="-5" y="1271.6358348968104" class="">ni2607</text>
              <title>0.3109756098</title>
            </g>
            <g class="guides">
              <text x="-5" y="1249.8722326454033" class="">ru2609</text>
              <title>0.3231707317</title>
            </g>
            <g class="guides">
              <text x="-5" y="1228.1086303939962" class="">bu2609</text>
              <title>0.3353658537</title>
            </g>
            <g class="guides">
              <text x="-5" y="1206.3450281425892" class="">y2609</text>
              <title>0.3475609756</title>
            </g>
            <g class="guides">
              <text x="-5" y="1184.5814258911819" class="">T2609</text>
              <title>0.3597560976</title>
            </g>
            <g class="guides">
              <text x="-5" y="1162.8178236397748" class="">i2609</text>
              <title>0.3719512195</title>
            </g>
            <g class="guides">
              <text x="-5" y="1141.0542213883675" class="">rr2607</text>
              <title>0.3841463415</title>
            </g>
            <g class="guides">
              <text x="-5" y="1119.2906191369605" class="">TL2609</text>
              <title>0.3963414634</title>
            </g>
            <g class="guides">
              <text x="-5" y="1097.5270168855534" class="">TF2609</text>
              <title>0.4085365854</title>
            </g>
            <g class="guides">
              <text x="-5" y="1075.7634146341463" class="">TS2609</text>
              <title>0.4207317073</title>
            </g>
            <g class="guides">
              <text x="-5" y="1053.9998123827393" class="">SH607</text>
              <title>0.4329268293</title>
            </g>
            <g class="guides">
              <text x="-5" y="1032.236210131332" class="">cu2607</text>
              <title>0.4451219512</title>
            </g>
            <g class="guides">
              <text x="-5" y="1010.4726078799248" class="">bc2607</text>
              <title>0.4573170732</title>
            </g>
            <g class="guides">
              <text x="-5" y="988.7090056285178" class="">m2609</text>
              <title>0.4695121951</title>
            </g>
            <g class="guides">
              <text x="-5" y="966.9454033771107" class="">ao2609</text>
              <title>0.4817073171</title>
            </g>
            <g class="guides">
              <text x="-5" y="945.1818011257035" class="">b2607</text>
              <title>0.493902439</title>
            </g>
            <g class="guides">
              <text x="-5" y="923.4181988742964" class="">hc2610</text>
              <title>0.506097561</title>
            </g>
            <g class="guides">
              <text x="-5" y="901.6545966228892" class="">pb2607</text>
              <title>0.5182926829</title>
            </g>
            <g class="guides">
              <text x="-5" y="879.8909943714822" class="">rb2610</text>
              <title>0.5304878049</title>
            </g>
            <g class="guides">
              <text x="-5" y="858.1273921200749" class="">SR609</text>
              <title>0.5426829268</title>
            </g>
            <g class="guides">
              <text x="-5" y="836.3637898686679" class="">bb2607</text>
              <title>0.5548780488</title>
            </g>
            <g class="guides">
              <text x="-5" y="814.6001876172609" class="">si2609</text>
              <title>0.5670731707</title>
            </g>
            <g class="guides">
              <text x="-5" y="792.8365853658536" class="">CF609</text>
              <title>0.5792682927</title>
            </g>
            <g class="guides">
              <text x="-5" y="771.0729831144467" class="">RS609</text>
              <title>0.5914634146</title>
            </g>
            <g class="guides">
              <text x="-5" y="749.3093808630395" class="">c2607</text>
              <title>0.6036585366</title>
            </g>
            <g class="guides">
              <text x="-5" y="727.5457786116322" class="">sp2609</text>
              <title>0.6158536585</title>
            </g>
            <g class="guides">
              <text x="-5" y="705.7821763602251" class="">CY607</text>
              <title>0.6280487805</title>
            </g>
            <g class="guides">
              <text x="-5" y="684.018574108818" class="">pp2609</text>
              <title>0.6402439024</title>
            </g>
            <g class="guides">
              <text x="-5" y="662.2549718574107" class="">ad2607</text>
              <title>0.6524390244</title>
            </g>
            <g class="guides">
              <text x="-5" y="640.4913696060037" class="">RM609</text>
              <title>0.6646341463</title>
            </g>
            <g class="guides">
              <text x="-5" y="618.7277673545964" class="">al2607</text>
              <title>0.6768292683</title>
            </g>
            <g class="guides">
              <text x="-5" y="596.9641651031895" class="">PL608</text>
              <title>0.6890243902</title>
            </g>
            <g class="guides">
              <text x="-5" y="575.2005628517825" class="">IF2606</text>
              <title>0.7012195122</title>
            </g>
            <g class="guides">
              <text x="-5" y="553.4369606003752" class="">au2608</text>
              <title>0.7134146341</title>
            </g>
            <g class="guides">
              <text x="-5" y="531.6733583489681" class="">l2609</text>
              <title>0.7256097561</title>
            </g>
            <g class="guides">
              <text x="-5" y="509.9097560975611" class="">eb2607</text>
              <title>0.737804878</title>
            </g>
            <g class="guides">
              <text x="-5" y="488.1461538461538" class="">sc2607</text>
              <title>0.75</title>
            </g>
            <g class="guides">
              <text x="-5" y="466.38255159474676" class="">bz2607</text>
              <title>0.762195122</title>
            </g>
            <g class="guides">
              <text x="-5" y="444.61894934333947" class="">wr2607</text>
              <title>0.7743902439</title>
            </g>
            <g class="guides">
              <text x="-5" y="422.85534709193263" class="">sn2607</text>
              <title>0.7865853659</title>
            </g>
            <g class="guides">
              <text x="-5" y="401.09174484052534" class="">lh2607</text>
              <title>0.7987804878</title>
            </g>
            <g class="guides">
              <text x="-5" y="379.32814258911804" class="">UR609</text>
              <title>0.8109756098</title>
            </g>
            <g class="guides">
              <text x="-5" y="357.5645403377112" class="">lc2609</text>
              <title>0.8231707317</title>
            </g>
            <g class="guides">
              <text x="-5" y="335.80093808630414" class="">zn2607</text>
              <title>0.8353658537</title>
            </g>
            <g class="guides">
              <text x="-5" y="314.03733583489685" class="">MA609</text>
              <title>0.8475609756</title>
            </g>
            <g class="guides">
              <text x="-5" y="292.2737335834898" class="">pd2608</text>
              <title>0.8597560976</title>
            </g>
            <g class="guides">
              <text x="-5" y="270.5101313320825" class="">IH2606</text>
              <title>0.8719512195</title>
            </g>
            <g class="guides">
              <text x="-5" y="248.74652908067543" class="">br2607</text>
              <title>0.8841463415</title>
            </g>
            <g class="guides">
              <text x="-5" y="226.98292682926837" class="">ps2609</text>
              <title>0.8963414634</title>
            </g>
            <g class="guides">
              <text x="-5" y="205.21932457786107" class="">eg2609</text>
              <title>0.9085365854</title>
            </g>
            <g class="guides">
              <text x="-5" y="183.455722326454" class="">IC2606</text>
              <title>0.9207317073</title>
            </g>
            <g class="guides">
              <text x="-5" y="161.69212007504694" class="">lu2607</text>
              <title>0.9329268293</title>
            </g>
            <g class="guides">
              <text x="-5" y="139.92851782363988" class="">IM2606</text>
              <title>0.9451219512</title>
            </g>
            <g class="guides">
              <text x="-5" y="118.1649155722328" class="">ag2608</text>
              <title>0.9573170732</title>
            </g>
            <g class="guides">
              <text x="-5" y="96.40131332082551" class="">fu2609</text>
              <title>0.9695121951</title>
            </g>
            <g class="guides">
              <text x="-5" y="74.63771106941844" class="">pt2608</text>
              <title>0.9817073171</title>
            </g>
            <g class="guides">
              <text x="-5" y="52.87410881801138" class="">pg2607</text>
              <title>0.993902439</title>
            </g>
          </g>
          <g class="axis x always_show">
            <g class="guides">
              <path d="M68.822358 0.000000 v1856.000000" class="guide line" />
              <text
                x="68.82235793163036"
                y="1875.0"
                class=""
                transform="rotate(90 68.822358 1875.000000)"
              >
                -0.03
              </text>
            </g>
            <g class="guides">
              <path d="M152.015878 0.000000 v1856.000000" class="guide line" />
              <text
                x="152.01587800074515"
                y="1875.0"
                class=""
                transform="rotate(90 152.015878 1875.000000)"
              >
                -0.02
              </text>
            </g>
            <g class="guides">
              <path d="M235.209398 0.000000 v1856.000000" class="guide line" />
              <text
                x="235.20939806985993"
                y="1875.0"
                class=""
                transform="rotate(90 235.209398 1875.000000)"
              >
                -0.01
              </text>
            </g>
            <g class="guides">
              <path
                d="M318.402918 0.000000 v1856.000000"
                class="axis major line"
              />
              <text
                x="318.4029181389748"
                y="1875.0"
                class="major"
                transform="rotate(90 318.402918 1875.000000)"
              >
                0
              </text>
            </g>
            <g class="guides">
              <path d="M401.596438 0.000000 v1856.000000" class="guide line" />
              <text
                x="401.59643820808964"
                y="1875.0"
                class=""
                transform="rotate(90 401.596438 1875.000000)"
              >
                0.01
              </text>
            </g>
            <g class="guides">
              <path d="M484.789958 0.000000 v1856.000000" class="guide line" />
              <text
                x="484.78995827720445"
                y="1875.0"
                class=""
                transform="rotate(90 484.789958 1875.000000)"
              >
                0.02
              </text>
            </g>
            <g class="guides">
              <path d="M567.983478 0.000000 v1856.000000" class="guide line" />
              <text
                x="567.9834783463192"
                y="1875.0"
                class=""
                transform="rotate(90 567.983478 1875.000000)"
              >
                0.03
              </text>
            </g>
          </g>
          <g class="series serie-0 color-0">
            <g class="bars">
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1799.8499061913697"
                  rx="0"
                  ry="0"
                  width="180.65712846769816"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.02171528844</desc>
                <desc class="x centered">408.7314823728239</desc>
                <desc class="y centered">1809.4258911819888</desc>
                <desc class="x_label">jd2608</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1778.0863039399624"
                  rx="0"
                  ry="0"
                  width="122.10399227365207"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01467710372</desc>
                <desc class="x centered">379.4549142758009</desc>
                <desc class="y centered">1787.6622889305816</desc>
                <desc class="x_label">FG609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1756.3227016885553"
                  rx="0"
                  ry="0"
                  width="104.4816578576017"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0125588697</desc>
                <desc class="x centered">370.6437470677757</desc>
                <desc class="y centered">1765.8986866791745</desc>
                <desc class="x_label">fb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1734.5590994371482"
                  rx="0"
                  ry="0"
                  width="102.39202470044933"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01230769231</desc>
                <desc class="x centered">369.59893048919946</desc>
                <desc class="y centered">1744.1350844277674</desc>
                <desc class="x_label">SF607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1712.795497185741"
                  rx="0"
                  ry="0"
                  width="95.56012440371336"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01148648649</desc>
                <desc class="x centered">366.1829803408315</desc>
                <desc class="y centered">1722.3714821763601</desc>
                <desc class="x_label">ec2606</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1691.0318949343339"
                  rx="0"
                  ry="0"
                  width="87.31289781204094"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01049515608</desc>
                <desc class="x centered">362.05936704499527</desc>
                <desc class="y centered">1700.607879924953</desc>
                <desc class="x_label">j2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1669.2682926829268"
                  rx="0"
                  ry="0"
                  width="85.8345841982927"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01031746032</desc>
                <desc class="x centered">361.32021023812115</desc>
                <desc class="y centered">1678.844277673546</desc>
                <desc class="x_label">jm2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1647.5046904315197"
                  rx="0"
                  ry="0"
                  width="58.685385335956084"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.00705408129</desc>
                <desc class="x centered">347.74561080695287</desc>
                <desc class="y centered">1657.080675422139</desc>
                <desc class="x_label">SM607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1625.7410881801125"
                  rx="0"
                  ry="0"
                  width="56.78151318057553"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.006825232678</desc>
                <desc class="x centered">346.7936747292626</desc>
                <desc class="y centered">1635.3170731707316</desc>
                <desc class="x_label">a2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1603.9774859287054"
                  rx="0"
                  ry="0"
                  width="50.50015733939438"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.00607020322</desc>
                <desc class="x centered">343.652996808672</desc>
                <desc class="y centered">1613.5534709193246</desc>
                <desc class="x_label">PF607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1582.2138836772983"
                  rx="0"
                  ry="0"
                  width="44.91668923919303"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.005399061033</desc>
                <desc class="x centered">340.86126275857134</desc>
                <desc class="y centered">1591.7898686679175</desc>
                <desc class="x_label">PX607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1560.4502814258913"
                  rx="0"
                  ry="0"
                  width="40.472523276866184"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004864864865</desc>
                <desc class="x centered">338.6391797774079</desc>
                <desc class="y centered">1570.0262664165105</desc>
                <desc class="x_label">CJ609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1538.686679174484"
                  rx="0"
                  ry="0"
                  width="39.452597146177254"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004742268041</desc>
                <desc class="x centered">338.12921671206345</desc>
                <desc class="y centered">1548.2626641651032</desc>
                <desc class="x_label">v2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1516.923076923077"
                  rx="0"
                  ry="0"
                  width="38.62479652422206"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004642765025</desc>
                <desc class="x centered">337.71531640108583</desc>
                <desc class="y centered">1526.499061913696</desc>
                <desc class="x_label">PR607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1495.1594746716698"
                  rx="0"
                  ry="0"
                  width="36.877338711375444"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004432717678</desc>
                <desc class="x centered">336.8415874946626</desc>
                <desc class="y centered">1504.735459662289</desc>
                <desc class="x_label">p2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1473.3958724202628"
                  rx="0"
                  ry="0"
                  width="36.46378155423099"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004383007417</desc>
                <desc class="x centered">336.6348089160903</desc>
                <desc class="y centered">1482.971857410882</desc>
                <desc class="x_label">ss2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1451.6322701688555"
                  rx="0"
                  ry="0"
                  width="35.94269727146923"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004320372217</desc>
                <desc class="x centered">336.37426677470944</desc>
                <desc class="y centered">1461.2082551594747</desc>
                <desc class="x_label">TA609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1429.8686679174484"
                  rx="0"
                  ry="0"
                  width="32.68900592106627"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003929273084</desc>
                <desc class="x centered">334.74742109950796</desc>
                <desc class="y centered">1439.4446529080676</desc>
                <desc class="x_label">PK610</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1408.1050656660414"
                  rx="0"
                  ry="0"
                  width="31.322861471804686"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003765060241</desc>
                <desc class="x centered">334.06434887487717</desc>
                <desc class="y centered">1417.6810506566605</desc>
                <desc class="x_label">cs2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1386.341463414634"
                  rx="0"
                  ry="0"
                  width="27.777469138268543"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003338898164</desc>
                <desc class="x centered">332.2916527081091</desc>
                <desc class="y centered">1395.9174484052533</desc>
                <desc class="x_label">SA609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1364.577861163227"
                  rx="0"
                  ry="0"
                  width="25.884729330776622"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003111387679</desc>
                <desc class="x centered">331.34528280436314</desc>
                <desc class="y centered">1374.1538461538462</desc>
                <desc class="x_label">OI609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1342.81425891182"
                  rx="0"
                  ry="0"
                  width="25.554323570718395"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003071672355</desc>
                <desc class="x centered">331.180079924334</desc>
                <desc class="y centered">1352.3902439024391</desc>
                <desc class="x_label">nr2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1321.0506566604129"
                  rx="0"
                  ry="0"
                  width="25.226776026231107"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003032300593</desc>
                <desc class="x centered">331.01630615209035</desc>
                <desc class="y centered">1330.626641651032</desc>
                <desc class="x_label">AP610</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1299.2870544090056"
                  rx="0"
                  ry="0"
                  width="24.87100749450309"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.002989536622</desc>
                <desc class="x centered">330.83842188622634</desc>
                <desc class="y centered">1308.8630393996248</desc>
                <desc class="x_label">op2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1277.5234521575985"
                  rx="0"
                  ry="0"
                  width="20.643553367025277"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.002481389578</desc>
                <desc class="x centered">328.72469482248744</desc>
                <desc class="y centered">1287.0994371482177</desc>
                <desc class="x_label">lg2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1255.7598499061912"
                  rx="0"
                  ry="0"
                  width="15.66295963925836"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001882713897</desc>
                <desc class="x centered">326.234397958604</desc>
                <desc class="y centered">1265.3358348968104</desc>
                <desc class="x_label">ni2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1233.9962476547842"
                  rx="0"
                  ry="0"
                  width="14.372620800882714"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001727613015</desc>
                <desc class="x centered">325.5892285394162</desc>
                <desc class="y centered">1243.5722326454033</desc>
                <desc class="x_label">ru2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1212.232645403377"
                  rx="0"
                  ry="0"
                  width="10.006437342928734"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001202790474</desc>
                <desc class="x centered">323.4061368104392</desc>
                <desc class="y centered">1221.8086303939963</desc>
                <desc class="x_label">bu2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1190.46904315197"
                  rx="0"
                  ry="0"
                  width="8.878710786457987"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001067235859</desc>
                <desc class="x centered">322.8422735322038</desc>
                <desc class="y centered">1200.0450281425892</desc>
                <desc class="x_label">y2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1168.705440900563"
                  rx="0"
                  ry="0"
                  width="7.639090957174119"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0009182314862</desc>
                <desc class="x centered">322.22246361756186</desc>
                <desc class="y centered">1178.2814258911822</desc>
                <desc class="x_label">T2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1146.941838649156"
                  rx="0"
                  ry="0"
                  width="5.326089633105539"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0006402048656</desc>
                <desc class="x centered">321.0659629555276</desc>
                <desc class="y centered">1156.517823639775</desc>
                <desc class="x_label">i2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1125.1782363977484"
                  rx="0"
                  ry="0"
                  width="4.69887150912831"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0005648121999</desc>
                <desc class="x centered">320.75235389353895</desc>
                <desc class="y centered">1134.7542213883676</desc>
                <desc class="x_label">rr2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1103.4146341463413"
                  rx="0"
                  ry="0"
                  width="3.6623313994152227"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0004402183483</desc>
                <desc class="x centered">320.2340838386824</desc>
                <desc class="y centered">1112.9906191369605</desc>
                <desc class="x_label">TL2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1081.6510318949342"
                  rx="0"
                  ry="0"
                  width="2.740105587370124"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0003293652661</desc>
                <desc class="x centered">319.77297093265986</desc>
                <desc class="y centered">1091.2270168855534</desc>
                <desc class="x_label">TF2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1059.8874296435272"
                  rx="0"
                  ry="0"
                  width="0.8106791922702996"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">9.74449923e-05</desc>
                <desc class="x centered">318.80825773511</desc>
                <desc class="y centered">1069.4634146341464</desc>
                <desc class="x_label">TS2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #ef4444; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1038.1238273921201"
                  rx="0"
                  ry="0"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0</desc>
                <desc class="x centered">318.4029181389748</desc>
                <desc class="y centered">1047.6998123827393</desc>
                <desc class="x_label">SH607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="317.6082527452491"
                  y="1016.3602251407132"
                  rx="0"
                  ry="0"
                  width="0.7946653937257224"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-9.552010698e-05</desc>
                <desc class="x centered">318.00558544211196</desc>
                <desc class="y centered">1025.9362101313322</desc>
                <desc class="x_label">cu2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="316.613810180499"
                  y="994.5966228893058"
                  rx="0"
                  ry="0"
                  width="1.7891079584758245"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0002150537634</desc>
                <desc class="x centered">317.5083641597369</desc>
                <desc class="y centered">1004.1726078799248</desc>
                <desc class="x_label">bc2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="315.6036745296508"
                  y="972.8330206378987"
                  rx="0"
                  ry="0"
                  width="2.799243609324037"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.000336473755</desc>
                <desc class="x centered">317.00329633431284</desc>
                <desc class="y centered">982.4090056285178</desc>
                <desc class="x_label">m2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="315.4889594675522"
                  y="951.0694183864915"
                  rx="0"
                  ry="0"
                  width="2.9139586714226198"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.000350262697</desc>
                <desc class="x centered">316.9459388032635</desc>
                <desc class="y centered">960.6454033771106</desc>
                <desc class="x_label">ao2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="313.72386751641505"
                  y="929.3058161350845"
                  rx="0"
                  ry="0"
                  width="4.679050622559771"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0005624296963</desc>
                <desc class="x centered">316.06339282769494</desc>
                <desc class="y centered">938.8818011257035</desc>
                <desc class="x_label">b2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="313.4582809877644"
                  y="907.5422138836773"
                  rx="0"
                  ry="0"
                  width="4.944637151210429"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0005943536404</desc>
                <desc class="x centered">315.9305995633696</desc>
                <desc class="y centered">917.1181988742964</desc>
                <desc class="x_label">hc2610</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="313.43317380987577"
                  y="885.7786116322702"
                  rx="0"
                  ry="0"
                  width="4.969744329099058"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0005973715651</desc>
                <desc class="x centered">315.9180459744253</desc>
                <desc class="y centered">895.3545966228893</desc>
                <desc class="x_label">pb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="313.11407388791815"
                  y="864.0150093808629"
                  rx="0"
                  ry="0"
                  width="5.288844251056673"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0006357279085</desc>
                <desc class="x centered">315.75849601344646</desc>
                <desc class="y centered">873.590994371482</desc>
                <desc class="x_label">rb2610</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="310.6812251680152"
                  y="842.251407129456"
                  rx="0"
                  ry="0"
                  width="7.721692970959623"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0009281603861</desc>
                <desc class="x centered">314.542071653495</desc>
                <desc class="y centered">851.827392120075</desc>
                <desc class="x_label">SR609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="309.95687549236357"
                  y="820.4878048780487"
                  rx="0"
                  ry="0"
                  width="8.44604264661126"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001015228426</desc>
                <desc class="x centered">314.17989681566917</desc>
                <desc class="y centered">830.0637898686678</desc>
                <desc class="x_label">bb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="303.84162524473095"
                  y="798.7242026266415"
                  rx="0"
                  ry="0"
                  width="14.561292894243877"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001750291715</desc>
                <desc class="x centered">311.1222716918529</desc>
                <desc class="y centered">808.3001876172606</desc>
                <desc class="x_label">si2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="302.87691128315225"
                  y="776.9606003752347"
                  rx="0"
                  ry="0"
                  width="15.526006855822573"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001866251944</desc>
                <desc class="x centered">310.6399147110635</desc>
                <desc class="y centered">786.5365853658537</desc>
                <desc class="x_label">CF609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="290.95584605505115"
                  y="755.1969981238274"
                  rx="0"
                  ry="0"
                  width="27.447072083923672"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003299183886</desc>
                <desc class="x centered">304.679382097013</desc>
                <desc class="y centered">764.7729831144464</desc>
                <desc class="x_label">RS609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="286.12956983630096"
                  y="733.4333958724203"
                  rx="0"
                  ry="0"
                  width="32.27334830267387"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003879310345</desc>
                <desc class="x centered">302.2662439876379</desc>
                <desc class="y centered">743.0093808630394</desc>
                <desc class="x_label">c2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="285.04545219305834"
                  y="711.6697936210132"
                  rx="0"
                  ry="0"
                  width="33.35746594591649"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.004009623095</desc>
                <desc class="x centered">301.7241851660166</desc>
                <desc class="y centered">721.2457786116323</desc>
                <desc class="x_label">sp2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="282.9060198386566"
                  y="689.906191369606"
                  rx="0"
                  ry="0"
                  width="35.49689830031821"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.004266786436</desc>
                <desc class="x centered">300.6544689888157</desc>
                <desc class="y centered">699.482176360225</desc>
                <desc class="x_label">CY607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="277.23741574850783"
                  y="668.1425891181987"
                  rx="0"
                  ry="0"
                  width="41.165502390467"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.004948162111</desc>
                <desc class="x centered">297.82016694374136</desc>
                <desc class="y centered">677.7185741088177</desc>
                <desc class="x_label">pp2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="277.0756835474061"
                  y="646.3789868667918"
                  rx="0"
                  ry="0"
                  width="41.327234591568754"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.004967602592</desc>
                <desc class="x centered">297.73930084319045</desc>
                <desc class="y centered">655.9549718574109</desc>
                <desc class="x_label">ad2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="274.9598267190713"
                  y="624.6153846153845"
                  rx="0"
                  ry="0"
                  width="43.44309141990351"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.005221932115</desc>
                <desc class="x centered">296.6813724290231</desc>
                <desc class="y centered">634.1913696060036</desc>
                <desc class="x_label">RM609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="269.42581537802647"
                  y="602.8517823639775"
                  rx="0"
                  ry="0"
                  width="48.977102760948355"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.005887129517</desc>
                <desc class="x centered">293.91436675850065</desc>
                <desc class="y centered">612.4277673545965</desc>
                <desc class="x_label">al2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="268.96104447752407"
                  y="581.0881801125702"
                  rx="0"
                  ry="0"
                  width="49.44187366145076"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.005942995755</desc>
                <desc class="x centered">293.6819813082494</desc>
                <desc class="y centered">590.6641651031892</desc>
                <desc class="x_label">PL608</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="249.1032934182744"
                  y="559.3245778611633"
                  rx="0"
                  ry="0"
                  width="69.29962472070042"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.008329930584</desc>
                <desc class="x centered">283.7531057786246</desc>
                <desc class="y centered">568.9005628517824</desc>
                <desc class="x_label">IF2606</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="248.78561160643378"
                  y="537.5609756097563"
                  rx="0"
                  ry="0"
                  width="69.61730653254105"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.008368116468</desc>
                <desc class="x centered">283.5942648727043</desc>
                <desc class="y centered">547.1369606003753</desc>
                <desc class="x_label">au2608</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="246.98759661904236"
                  y="515.797373358349"
                  rx="0"
                  ry="0"
                  width="71.41532151993246"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.008584240871</desc>
                <desc class="x centered">282.6952573790086</desc>
                <desc class="y centered">525.373358348968</desc>
                <desc class="x_label">l2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="241.9226647557235"
                  y="494.0337711069417"
                  rx="0"
                  ry="0"
                  width="76.48025338325132"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.009193054137</desc>
                <desc class="x centered">280.16279144734915</desc>
                <desc class="y centered">503.6097560975608</desc>
                <desc class="x_label">eb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="241.44822497956886"
                  y="472.27016885553485"
                  rx="0"
                  ry="0"
                  width="76.95469315940596"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00925008259</desc>
                <desc class="x centered">279.9255715592718</desc>
                <desc class="y centered">481.846153846154</desc>
                <desc class="x_label">sc2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="240.52895736234743"
                  y="450.50656660412756"
                  rx="0"
                  ry="0"
                  width="77.8739607766274"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.009360580092</desc>
                <desc class="x centered">279.4659377506611</desc>
                <desc class="y centered">460.0825515947467</desc>
                <desc class="x_label">bz2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="232.50990331835493"
                  y="428.74296435272026"
                  rx="0"
                  ry="0"
                  width="85.8930148206199"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01032448378</desc>
                <desc class="x centered">275.4564107286649</desc>
                <desc class="y centered">438.3189493433394</desc>
                <desc class="x_label">wr2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="231.39881381532555"
                  y="406.9793621013132"
                  rx="0"
                  ry="0"
                  width="87.00410432364927"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01045803859</desc>
                <desc class="x centered">274.9008659771502</desc>
                <desc class="y centered">416.55534709193233</desc>
                <desc class="x_label">sn2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="229.57046866870377"
                  y="385.21575984990614"
                  rx="0"
                  ry="0"
                  width="88.83244947027106"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01067780873</desc>
                <desc class="x centered">273.9866934038393</desc>
                <desc class="y centered">394.79174484052527</desc>
                <desc class="x_label">lh2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="226.355293194222"
                  y="363.45215759849907"
                  rx="0"
                  ry="0"
                  width="92.04762494475281"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01106427819</desc>
                <desc class="x centered">272.37910566659843</desc>
                <desc class="y centered">373.0281425891182</desc>
                <desc class="x_label">UR609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="223.32460948855766"
                  y="341.688555347092"
                  rx="0"
                  ry="0"
                  width="95.07830865041717"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01142857143</desc>
                <desc class="x centered">270.86376381376624</desc>
                <desc class="y centered">351.26454033771114</desc>
                <desc class="x_label">lc2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="200.5744735966418"
                  y="319.9249530956847"
                  rx="0"
                  ry="0"
                  width="117.82844454233302"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01416317574</desc>
                <desc class="x centered">259.4886958678083</desc>
                <desc class="y centered">329.50093808630385</desc>
                <desc class="x_label">zn2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="198.51067480562787"
                  y="298.1613508442779"
                  rx="0"
                  ry="0"
                  width="119.89224333334695"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0144112478</desc>
                <desc class="x centered">258.45679647230133</desc>
                <desc class="y centered">307.737335834897</desc>
                <desc class="x_label">MA609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="198.44199281261564"
                  y="276.3977485928706"
                  rx="0"
                  ry="0"
                  width="119.96092532635919"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01441950349</desc>
                <desc class="x centered">258.42245547579523</desc>
                <desc class="y centered">285.9737335834897</desc>
                <desc class="x_label">pd2608</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="193.9645564789121"
                  y="254.6341463414633"
                  rx="0"
                  ry="0"
                  width="124.43836166006272"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01495769882</desc>
                <desc class="x centered">256.1837373089435</desc>
                <desc class="y centered">264.2101313320824</desc>
                <desc class="x_label">IH2606</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="192.17826699962848"
                  y="232.87054409005648"
                  rx="0"
                  ry="0"
                  width="126.22465113934635"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01517241379</desc>
                <desc class="x centered">255.29059256930165</desc>
                <desc class="y centered">242.44652908067562</desc>
                <desc class="x_label">br2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="178.11405935005024"
                  y="211.1069418386492"
                  rx="0"
                  ry="0"
                  width="140.28885878892459"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01686295503</desc>
                <desc class="x centered">248.25848874451253</desc>
                <desc class="y centered">220.68292682926833</desc>
                <desc class="x_label">ps2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="175.66893762823818"
                  y="189.3433395872419"
                  rx="0"
                  ry="0"
                  width="142.73398051073664"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01715686275</desc>
                <desc class="x centered">247.03592788360652</desc>
                <desc class="y centered">198.91932457786103</desc>
                <desc class="x_label">eg2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="172.52775219943345"
                  y="167.57973733583484"
                  rx="0"
                  ry="0"
                  width="145.87516593954138"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01753443848</desc>
                <desc class="x centered">245.46533516920414</desc>
                <desc class="y centered">177.15572232645397</desc>
                <desc class="x_label">IC2606</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="158.68247059392937"
                  y="145.81613508442777"
                  rx="0"
                  ry="0"
                  width="159.72044754504546"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01919866444</desc>
                <desc class="x centered">238.5426943664521</desc>
                <desc class="y centered">155.3921200750469</desc>
                <desc class="x_label">lu2607</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="152.46019495455704"
                  y="124.05253283302069"
                  rx="0"
                  ry="0"
                  width="165.9427231844178"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01994659236</desc>
                <desc class="x centered">235.43155654676593</desc>
                <desc class="y centered">133.62851782363984</desc>
                <desc class="x_label">IM2606</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="151.78359368783754"
                  y="102.28893058161363"
                  rx="0"
                  ry="0"
                  width="166.6193244511373"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.02002792096</desc>
                <desc class="x centered">235.09325591340618</desc>
                <desc class="y centered">111.86491557223277</desc>
                <desc class="x_label">ag2608</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="127.6707366307001"
                  y="80.52532833020634"
                  rx="0"
                  ry="0"
                  width="190.73218150827472"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.02292632664</desc>
                <desc class="x centered">223.03682738483747</desc>
                <desc class="y centered">90.10131332082548</desc>
                <desc class="x_label">fu2609</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="119.49330644823237"
                  y="58.7617260787995"
                  rx="0"
                  ry="0"
                  width="198.90961169074245"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0239092674</desc>
                <desc class="x centered">218.9481122936036</desc>
                <desc class="y centered">68.33771106941865</desc>
                <desc class="x_label">pt2608</desc>
              </g>
              <g
                class="bar"
                style="fill: #22c55e; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="63.90797277986817"
                  y="36.998123827392206"
                  rx="0"
                  ry="0"
                  width="254.49494535910665"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0305907173</desc>
                <desc class="x centered">191.1554454594215</desc>
                <desc class="y centered">46.57410881801135</desc>
                <desc class="x_label">pg2607</desc>
              </g>
            </g>
          </g>
          <g class="series serie-1 color-1">
            <g class="bars">
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="499.060046606673"
                  y="1799.8499061913697"
                  rx="0"
                  ry="0"
                  width="52.919764904679425"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.006361044089</desc>
                <desc class="x centered">525.5199290590127</desc>
                <desc class="y centered">1809.4258911819888</desc>
                <desc class="x_label">jd2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="440.5069104126269"
                  y="1778.0863039399624"
                  rx="0"
                  ry="0"
                  width="48.84159690946075"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.005870841487</desc>
                <desc class="x centered">464.9277088673573</desc>
                <desc class="y centered">1787.6622889305816</desc>
                <desc class="x_label">FG609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="422.88457599657653"
                  y="1756.3227016885553"
                  rx="0"
                  ry="0"
                  width="13.06020723220007"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001569858713</desc>
                <desc class="x centered">429.41467961267654</desc>
                <desc class="y centered">1765.8986866791745</desc>
                <desc class="x_label">fb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="420.79494283942415"
                  y="1734.5590994371482"
                  rx="0"
                  ry="0"
                  width="2.8442229083458415"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0003418803419</desc>
                <desc class="x centered">422.2170542935971</desc>
                <desc class="y centered">1744.1350844277674</desc>
                <desc class="x_label">SF607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="413.9630425426882"
                  y="1712.795497185741"
                  rx="0"
                  ry="0"
                  width="71.67009330278466"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.008614864865</desc>
                <desc class="x centered">449.7980891940805</desc>
                <desc class="y centered">1722.3714821763601</desc>
                <desc class="x_label">ec2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="405.71581595101577"
                  y="1691.0318949343339"
                  rx="0"
                  ry="0"
                  width="11.193961257954129"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001345532831</desc>
                <desc class="x centered">411.31279657999283</desc>
                <desc class="y centered">1700.607879924953</desc>
                <desc class="x_label">j2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="404.23750233726753"
                  y="1669.2682926829268"
                  rx="0"
                  ry="0"
                  width="59.423942906510604"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.007142857143</desc>
                <desc class="x centered">433.9494737905228</desc>
                <desc class="y centered">1678.844277673546</desc>
                <desc class="x_label">jm2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="377.0883034749309"
                  y="1647.5046904315197"
                  rx="0"
                  ry="0"
                  width="16.767252953130253"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.002015451797</desc>
                <desc class="x centered">385.471929951496</desc>
                <desc class="y centered">1657.080675422139</desc>
                <desc class="x_label">SM607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="375.18443131955036"
                  y="1625.7410881801125"
                  rx="0"
                  ry="0"
                  width="10.323911487377188"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001240951396</desc>
                <desc class="x centered">380.3463870632389</desc>
                <desc class="y centered">1635.3170731707316</desc>
                <desc class="x_label">a2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="368.9030754783692"
                  y="1603.9774859287054"
                  rx="0"
                  ry="0"
                  width="13.173954088537585"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001583531275</desc>
                <desc class="x centered">375.490052522638</desc>
                <desc class="y centered">1613.5534709193246</desc>
                <desc class="x_label">PF607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="363.31960737816786"
                  y="1582.2138836772983"
                  rx="0"
                  ry="0"
                  width="37.10509111063806"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004460093897</desc>
                <desc class="x centered">381.87215293348686</desc>
                <desc class="y centered">1591.7898686679175</desc>
                <desc class="x_label">PX607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="358.875441415841"
                  y="1560.4502814258913"
                  rx="0"
                  ry="0"
                  width="71.95115249220748"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.008648648649</desc>
                <desc class="x centered">394.85101766194475</desc>
                <desc class="y centered">1570.0262664165105</desc>
                <desc class="x_label">CJ609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="357.8555152851521"
                  y="1538.686679174484"
                  rx="0"
                  ry="0"
                  width="53.17523963180537"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.006391752577</desc>
                <desc class="x centered">384.44313510105474</desc>
                <desc class="y centered">1548.2626641651032</desc>
                <desc class="x_label">v2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="357.0277146631969"
                  y="1516.923076923077"
                  rx="0"
                  ry="0"
                  width="49.35390666983858"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.005932421976</desc>
                <desc class="x centered">381.7046679981162</desc>
                <desc class="y centered">1526.499061913696</desc>
                <desc class="x_label">PR607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="355.28025685035027"
                  y="1495.1594746716698"
                  rx="0"
                  ry="0"
                  width="54.437976192982774"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.00654353562</desc>
                <desc class="x centered">382.49924494684166</desc>
                <desc class="y centered">1504.735459662289</desc>
                <desc class="x_label">p2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="354.8666996932058"
                  y="1473.3958724202628"
                  rx="0"
                  ry="0"
                  width="78.53737565526683"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.009440323668</desc>
                <desc class="x centered">394.13538752083923</desc>
                <desc class="y centered">1482.971857410882</desc>
                <desc class="x_label">ss2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="354.34561541044405"
                  y="1451.6322701688555"
                  rx="0"
                  ry="0"
                  width="30.413051537396598"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003655699568</desc>
                <desc class="x centered">369.5521411791424</desc>
                <desc class="y centered">1461.2082551594747</desc>
                <desc class="x_label">TA609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="351.0919240600411"
                  y="1429.8686679174484"
                  rx="0"
                  ry="0"
                  width="18.38756583060001"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.00221021611</desc>
                <desc class="x centered">360.2857069753411</desc>
                <desc class="y centered">1439.4446529080676</desc>
                <desc class="x_label">PK610</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="349.7257796107795"
                  y="1408.1050656660414"
                  rx="0"
                  ry="0"
                  width="46.98429220770794"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.005647590361</desc>
                <desc class="x centered">373.21792571463345</desc>
                <desc class="y centered">1417.6810506566605</desc>
                <desc class="x_label">cs2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="346.18038727724337"
                  y="1386.341463414634"
                  rx="0"
                  ry="0"
                  width="55.554938276537484"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.006677796327</desc>
                <desc class="x centered">373.9578564155121</desc>
                <desc class="y centered">1395.9174484052533</desc>
                <desc class="x_label">SA609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="344.28764746975145"
                  y="1364.577861163227"
                  rx="0"
                  ry="0"
                  width="50.04381003950073"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.006015349513</desc>
                <desc class="x centered">369.3095524895018</desc>
                <desc class="y centered">1374.1538461538462</desc>
                <desc class="x_label">OI609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="343.9572417096932"
                  y="1342.81425891182"
                  rx="0"
                  ry="0"
                  width="229.98891213646073"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.02764505119</desc>
                <desc class="x centered">458.9516977779236</desc>
                <desc class="y centered">1352.3902439024391</desc>
                <desc class="x_label">nr2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="343.62969416520593"
                  y="1321.0506566604129"
                  rx="0"
                  ry="0"
                  width="24.129959677264708"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.002900461437</desc>
                <desc class="x centered">355.69467400383826</desc>
                <desc class="y centered">1330.626641651032</desc>
                <desc class="x_label">AP610</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="343.2739256334779"
                  y="1299.2870544090056"
                  rx="0"
                  ry="0"
                  width="24.871007494503715"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.002989536622</desc>
                <desc class="x centered">355.7094293807298</desc>
                <desc class="y centered">1308.8630393996248</desc>
                <desc class="x_label">op2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="339.0464715060001"
                  y="1277.5234521575985"
                  rx="0"
                  ry="0"
                  width="10.321776683512951"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001240694789</desc>
                <desc class="x centered">344.2073598477566</desc>
                <desc class="y centered">1287.0994371482177</desc>
                <desc class="x_label">lg2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="334.0658777782332"
                  y="1255.7598499061912"
                  rx="0"
                  ry="0"
                  width="128.78433481168315"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01548009204</desc>
                <desc class="x centered">398.45804518407476</desc>
                <desc class="y centered">1265.3358348968104</desc>
                <desc class="x_label">ni2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="332.77553893985754"
                  y="1233.9962476547842"
                  rx="0"
                  ry="0"
                  width="182.0531968111929"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.02188309819</desc>
                <desc class="x centered">423.80213734545396</desc>
                <desc class="y centered">1243.5722326454033</desc>
                <desc class="x_label">ru2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="328.40935548190356"
                  y="1212.232645403377"
                  rx="0"
                  ry="0"
                  width="88.05664861777848"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01058455617</desc>
                <desc class="x centered">372.4376797907928</desc>
                <desc class="y centered">1221.8086303939963</desc>
                <desc class="x_label">bu2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="327.2816289254328"
                  y="1190.46904315197"
                  rx="0"
                  ry="0"
                  width="32.55527288368063"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.00391319815</desc>
                <desc class="x centered">343.55926536727316</desc>
                <desc class="y centered">1200.0450281425892</desc>
                <desc class="x_label">y2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="326.04200909614894"
                  y="1168.705440900563"
                  rx="0"
                  ry="0"
                  width="1.9097727392941692"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0002295578715</desc>
                <desc class="x centered">326.996895465796</desc>
                <desc class="y centered">1178.2814258911822</desc>
                <desc class="x_label">T2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="323.72900777208037"
                  y="1146.941838649156"
                  rx="0"
                  ry="0"
                  width="37.28262743174167"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004481434059</desc>
                <desc class="x centered">342.3703214879512</desc>
                <desc class="y centered">1156.517823639775</desc>
                <desc class="x_label">i2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="323.10178964810314"
                  y="1125.1782363977484"
                  rx="0"
                  ry="0"
                  width="9.397743018256335"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0011296244</desc>
                <desc class="x centered">327.8006611572313</desc>
                <desc class="y centered">1134.7542213883676</desc>
                <desc class="x_label">rr2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="322.06524953839005"
                  y="1103.4146341463413"
                  rx="0"
                  ry="0"
                  width="9.522061638480068"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001144567706</desc>
                <desc class="x centered">326.8262803576301</desc>
                <desc class="y centered">1112.9906191369605</desc>
                <desc class="x_label">TL2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="321.14302372634495"
                  y="1081.6510318949342"
                  rx="0"
                  ry="0"
                  width="0.39144365533934433"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">4.705218087e-05</desc>
                <desc class="x centered">321.3387455540146</desc>
                <desc class="y centered">1091.2270168855534</desc>
                <desc class="x_label">TF2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="319.2135973312451"
                  y="1059.8874296435272"
                  rx="0"
                  ry="0"
                  width="0.9728150307238934"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0001169339908</desc>
                <desc class="x centered">319.70000484660704</desc>
                <desc class="y centered">1069.4634146341464</desc>
                <desc class="x_label">TS2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1038.1238273921201"
                  rx="0"
                  ry="0"
                  width="131.64875559686362"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0158244002</desc>
                <desc class="x centered">384.22729593740667</desc>
                <desc class="y centered">1047.6998123827393</desc>
                <desc class="x_label">SH607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="1016.3602251407132"
                  rx="0"
                  ry="0"
                  width="60.39456992313228"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.007259528131</desc>
                <desc class="x centered">348.60020310054097</desc>
                <desc class="y centered">1025.9362101313322</desc>
                <desc class="x_label">cu2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="994.5966228893058"
                  rx="0"
                  ry="0"
                  width="58.146008650456565"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.006989247312</desc>
                <desc class="x centered">347.4759224642031</desc>
                <desc class="y centered">1004.1726078799248</desc>
                <desc class="x_label">bc2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="972.8330206378987"
                  rx="0"
                  ry="0"
                  width="25.1931924839177"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003028263795</desc>
                <desc class="x centered">330.99951438093365</desc>
                <desc class="y centered">982.4090056285178</desc>
                <desc class="x_label">m2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="951.0694183864915"
                  rx="0"
                  ry="0"
                  width="125.30022287117117"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01506129597</desc>
                <desc class="x centered">381.0530295745604</desc>
                <desc class="y centered">960.6454033771106</desc>
                <desc class="x_label">ao2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="929.3058161350845"
                  rx="0"
                  ry="0"
                  width="28.074303735359308"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003374578178</desc>
                <desc class="x centered">332.4400700066545</desc>
                <desc class="y centered">938.8818011257035</desc>
                <desc class="x_label">b2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="907.5422138836773"
                  rx="0"
                  ry="0"
                  width="17.30623002923636"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.002080237741</desc>
                <desc class="x centered">327.05603315359303</desc>
                <desc class="y centered">917.1181988742964</desc>
                <desc class="x_label">hc2610</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="885.7786116322702"
                  rx="0"
                  ry="0"
                  width="34.788210303691926"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004181600956</desc>
                <desc class="x centered">335.7970232908208</desc>
                <desc class="y centered">895.3545966228893</desc>
                <desc class="x_label">pb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="864.0150093808629"
                  rx="0"
                  ry="0"
                  width="15.866532753168713"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001907183725</desc>
                <desc class="x centered">326.3361845155592</desc>
                <desc class="y centered">873.590994371482</desc>
                <desc class="x_label">rb2610</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="842.251407129456"
                  rx="0"
                  ry="0"
                  width="32.43111047802876"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003898273622</desc>
                <desc class="x centered">334.6184733779892</desc>
                <desc class="y centered">851.827392120075</desc>
                <desc class="x_label">SR609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="820.4878048780487"
                  rx="0"
                  ry="0"
                  width="8.446042646610977"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001015228426</desc>
                <desc class="x centered">322.6259394622803</desc>
                <desc class="y centered">830.0637898686678</desc>
                <desc class="x_label">bb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="798.7242026266415"
                  rx="0"
                  ry="0"
                  width="101.9290502597089"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01225204201</desc>
                <desc class="x centered">369.3674432688293</desc>
                <desc class="y centered">808.3001876172606</desc>
                <desc class="x_label">si2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="776.9606003752347"
                  rx="0"
                  ry="0"
                  width="49.16568837677079"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.005909797823</desc>
                <desc class="x centered">342.98576232736025</desc>
                <desc class="y centered">786.5365853658537</desc>
                <desc class="x_label">CF609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="755.1969981238274"
                  rx="0"
                  ry="0"
                  width="23.113323860146465"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.002778260115</desc>
                <desc class="x centered">329.95958006904806</desc>
                <desc class="y centered">764.7729831144464</desc>
                <desc class="x_label">RS609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="733.4333958724203"
                  rx="0"
                  ry="0"
                  width="14.343710356743884"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001724137931</desc>
                <desc class="x centered">325.57477331734674</desc>
                <desc class="y centered">743.0093808630394</desc>
                <desc class="x_label">c2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="711.6697936210132"
                  rx="0"
                  ry="0"
                  width="10.007239783774764"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001202886929</desc>
                <desc class="x centered">323.4065380308622</desc>
                <desc class="y centered">721.2457786116323</desc>
                <desc class="x_label">sp2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="689.906191369606"
                  rx="0"
                  ry="0"
                  width="31.760382689758558"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003817651022</desc>
                <desc class="x centered">334.2831094838541</desc>
                <desc class="y centered">699.482176360225</desc>
                <desc class="x_label">CY607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="668.1425891181987"
                  rx="0"
                  ry="0"
                  width="137.218341301556"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0164938737</desc>
                <desc class="x centered">387.01208878975285</desc>
                <desc class="y centered">677.7185741088177</desc>
                <desc class="x_label">pp2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="646.3789868667918"
                  rx="0"
                  ry="0"
                  width="26.952544298849205"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003239740821</desc>
                <desc class="x centered">331.8791902883994</desc>
                <desc class="y centered">655.9549718574109</desc>
                <desc class="x_label">ad2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="624.6153846153845"
                  rx="0"
                  ry="0"
                  width="14.481030473301018"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001740644038</desc>
                <desc class="x centered">325.64343337562536</desc>
                <desc class="y centered">634.1913696060036</desc>
                <desc class="x_label">RM609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="602.8517823639775"
                  rx="0"
                  ry="0"
                  width="13.510924899572046"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001624035729</desc>
                <desc class="x centered">325.15838058876085</desc>
                <desc class="y centered">612.4277673545965</desc>
                <desc class="x_label">al2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="581.0881801125702"
                  rx="0"
                  ry="0"
                  width="90.81160468429755"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01091570649</desc>
                <desc class="x centered">363.8087204811236</desc>
                <desc class="y centered">590.6641651031892</desc>
                <desc class="x_label">PL608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="559.3245778611633"
                  rx="0"
                  ry="0"
                  width="51.635014497775785"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.006206614945</desc>
                <desc class="x centered">344.22042538786275</desc>
                <desc class="y centered">568.9005628517824</desc>
                <desc class="x_label">IF2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="537.5609756097563"
                  rx="0"
                  ry="0"
                  width="27.008159883708515"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003246425907</desc>
                <desc class="x centered">331.9069980808291</desc>
                <desc class="y centered">547.1369606003753</desc>
                <desc class="x_label">au2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="515.797373358349"
                  rx="0"
                  ry="0"
                  width="62.88811895038782"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.007559256887</desc>
                <desc class="x centered">349.84697761416874</desc>
                <desc class="y centered">525.373358348968</desc>
                <desc class="x_label">l2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="494.0337711069417"
                  rx="0"
                  ry="0"
                  width="66.09404613367423"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.007944614686</desc>
                <desc class="x centered">351.4499412058119</desc>
                <desc class="y centered">503.6097560975608</desc>
                <desc class="x_label">eb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="472.27016885553485"
                  rx="0"
                  ry="0"
                  width="107.186894043459"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01288404361</desc>
                <desc class="x centered">371.99636516070433</desc>
                <desc class="y centered">481.846153846154</desc>
                <desc class="x_label">sc2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="450.50656660412756"
                  rx="0"
                  ry="0"
                  width="96.51983870905866"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01160184575</desc>
                <desc class="x centered">366.6628374935042</desc>
                <desc class="y centered">460.0825515947467</desc>
                <desc class="x_label">bz2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="428.74296435272026"
                  rx="0"
                  ry="0"
                  width="34.35720592824799"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.00412979351</desc>
                <desc class="x centered">335.5815211030988</desc>
                <desc class="y centered">438.3189493433394</desc>
                <desc class="x_label">wr2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="406.9793621013132"
                  rx="0"
                  ry="0"
                  width="87.19961916482623"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0104815398</desc>
                <desc class="x centered">362.00272772138794</desc>
                <desc class="y centered">416.55534709193233</desc>
                <desc class="x_label">sn2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="385.21575984990614"
                  rx="0"
                  ry="0"
                  width="38.62280411750913"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.004642525534</desc>
                <desc class="x centered">337.7143201977294</desc>
                <desc class="y centered">394.79174484052527</desc>
                <desc class="x_label">lh2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="363.45215759849907"
                  rx="0"
                  ry="0"
                  width="30.68254164825089"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003688092729</desc>
                <desc class="x centered">333.74418896310027</desc>
                <desc class="y centered">373.0281425891182</desc>
                <desc class="x_label">UR609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="341.688555347092"
                  rx="0"
                  ry="0"
                  width="186.3534849548172"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.0224</desc>
                <desc class="x centered">411.5796606163834</desc>
                <desc class="y centered">351.26454033771114</desc>
                <desc class="x_label">lc2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="319.9249530956847"
                  rx="0"
                  ry="0"
                  width="3.3191111138684732"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.000398962697</desc>
                <desc class="x centered">320.06247369590903</desc>
                <desc class="y centered">329.50093808630385</desc>
                <desc class="x_label">zn2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="298.1613508442779"
                  rx="0"
                  ry="0"
                  width="70.18082536586127"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.008435852373</desc>
                <desc class="x centered">353.4933308219055</desc>
                <desc class="y centered">307.737335834897</desc>
                <desc class="x_label">MA609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="276.3977485928706"
                  rx="0"
                  ry="0"
                  width="27.207632548245442"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.003270402854</desc>
                <desc class="x centered">332.00673441309755</desc>
                <desc class="y centered">285.9737335834897</desc>
                <desc class="x_label">pd2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="254.6341463414633"
                  rx="0"
                  ry="0"
                  width="14.076737744351021"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001692047377</desc>
                <desc class="x centered">325.44128701115034</desc>
                <desc class="y centered">264.2101313320824</desc>
                <desc class="x_label">IH2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="232.87054409005648"
                  rx="0"
                  ry="0"
                  width="91.79974628316114"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01103448276</desc>
                <desc class="x centered">364.3027912805554</desc>
                <desc class="y centered">242.44652908067562</desc>
                <desc class="x_label">br2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="211.1069418386492"
                  rx="0"
                  ry="0"
                  width="53.443374776733265"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.006423982869</desc>
                <desc class="x centered">345.1246055273415</desc>
                <desc class="y centered">220.68292682926833</desc>
                <desc class="x_label">ps2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="189.3433395872419"
                  rx="0"
                  ry="0"
                  width="12.975816410066841"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.001559714795</desc>
                <desc class="x centered">324.89082634400825</desc>
                <desc class="y centered">198.91932457786103</desc>
                <desc class="x_label">eg2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="167.57973733583484"
                  rx="0"
                  ry="0"
                  width="89.54520838632322"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01076348354</desc>
                <desc class="x centered">363.17552233213644</desc>
                <desc class="y centered">177.15572232645397</desc>
                <desc class="x_label">IC2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="145.81613508442777"
                  rx="0"
                  ry="0"
                  width="131.94297840677638"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01585976628</desc>
                <desc class="x centered">384.37440734236304</desc>
                <desc class="y centered">155.3921200750469</desc>
                <desc class="x_label">lu2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="124.05253283302069"
                  rx="0"
                  ry="0"
                  width="50.033952624870324"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.006014164635</desc>
                <desc class="x centered">343.41989445140996</desc>
                <desc class="y centered">133.62851782363984</desc>
                <desc class="x_label">IM2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="102.28893058161363"
                  rx="0"
                  ry="0"
                  width="135.79698293068566"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01632302405</desc>
                <desc class="x centered">386.30140960431766</desc>
                <desc class="y centered">111.86491557223277</desc>
                <desc class="x_label">ag2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="80.52532833020634"
                  rx="0"
                  ry="0"
                  width="111.439027398093"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.01339515714</desc>
                <desc class="x centered">374.1224318380213</desc>
                <desc class="y centered">90.10131332082548</desc>
                <desc class="x_label">fu2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="58.7617260787995"
                  rx="0"
                  ry="0"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0</desc>
                <desc class="x centered">318.4029181389748</desc>
                <desc class="y centered">68.33771106941865</desc>
                <desc class="x_label">pt2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #ef4444; stroke-width: 3"
              >
                <rect
                  x="318.4029181389748"
                  y="36.998123827392206"
                  rx="0"
                  ry="0"
                  width="62.89242902552627"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0.007559774965</desc>
                <desc class="x centered">349.84913265173793</desc>
                <desc class="y centered">46.57410881801135</desc>
                <desc class="x_label">pg2607</desc>
              </g>
            </g>
          </g>
          <g class="series serie-2 color-2">
            <g class="bars">
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="551.9798115113524"
                  y="1799.8499061913697"
                  rx="0"
                  ry="0"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0</desc>
                <desc class="x centered">551.9798115113524</desc>
                <desc class="y centered">1809.4258911819888</desc>
                <desc class="x_label">jd2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="302.1223858358212"
                  y="1778.0863039399624"
                  rx="0"
                  ry="0"
                  width="16.28053230315362"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001956947162</desc>
                <desc class="x centered">310.26265198739804</desc>
                <desc class="y centered">1787.6622889305816</desc>
                <desc class="x_label">FG609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="315.13786633092474"
                  y="1756.3227016885553"
                  rx="0"
                  ry="0"
                  width="3.2650518080500888"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0003924646782</desc>
                <desc class="x centered">316.7703922349498</desc>
                <desc class="y centered">1765.8986866791745</desc>
                <desc class="x_label">fb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="304.18180359724573"
                  y="1734.5590994371482"
                  rx="0"
                  ry="0"
                  width="14.221114541729094"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001709401709</desc>
                <desc class="x centered">311.2923608681103</desc>
                <desc class="y centered">1744.1350844277674</desc>
                <desc class="x_label">SF607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="175.06273153340535"
                  y="1712.795497185741"
                  rx="0"
                  ry="0"
                  width="143.34018660556947"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01722972973</desc>
                <desc class="x centered">246.7328248361901</desc>
                <desc class="y centered">1722.3714821763601</desc>
                <desc class="x_label">ec2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="246.7615660880686"
                  y="1691.0318949343339"
                  rx="0"
                  ry="0"
                  width="71.64135205090622"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.008611410118</desc>
                <desc class="x centered">282.5822421135217</desc>
                <desc class="y centered">1700.607879924953</desc>
                <desc class="x_label">j2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="258.9789752324642"
                  y="1669.2682926829268"
                  rx="0"
                  ry="0"
                  width="59.423942906510604"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.007142857143</desc>
                <desc class="x centered">288.6909466857195</desc>
                <desc class="y centered">1678.844277673546</desc>
                <desc class="x_label">jm2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="307.2247495035546"
                  y="1647.5046904315197"
                  rx="0"
                  ry="0"
                  width="11.178168635420207"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001343634531</desc>
                <desc class="x centered">312.8138338212647</desc>
                <desc class="y centered">1657.080675422139</desc>
                <desc class="x_label">SM607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="308.0790066515976"
                  y="1625.7410881801125"
                  rx="0"
                  ry="0"
                  width="10.323911487377245"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001240951396</desc>
                <desc class="x centered">313.2409623952862</desc>
                <desc class="y centered">1635.3170731707316</desc>
                <desc class="x_label">a2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="289.85935094714335"
                  y="1603.9774859287054"
                  rx="0"
                  ry="0"
                  width="28.54356719183147"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003430984429</desc>
                <desc class="x centered">304.1311345430591</desc>
                <desc class="y centered">1613.5534709193246</desc>
                <desc class="x_label">PF607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="238.33403732128215"
                  y="1582.2138836772983"
                  rx="0"
                  ry="0"
                  width="80.06888081769267"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.009624413146</desc>
                <desc class="x centered">278.36847773012846</desc>
                <desc class="y centered">1591.7898686679175</desc>
                <desc class="x_label">PX607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="309.40902407744886"
                  y="1560.4502814258913"
                  rx="0"
                  ry="0"
                  width="8.993894061525964"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001081081081</desc>
                <desc class="x centered">313.9059711082118</desc>
                <desc class="y centered">1570.0262664165105</desc>
                <desc class="x_label">CJ609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="289.242302857017"
                  y="1538.686679174484"
                  rx="0"
                  ry="0"
                  width="29.160615281957803"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003505154639</desc>
                <desc class="x centered">303.8226104979959</desc>
                <desc class="y centered">1548.2626641651032</desc>
                <desc class="x_label">v2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="290.5072317603704"
                  y="1516.923076923077"
                  rx="0"
                  ry="0"
                  width="27.89568637860441"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003353108073</desc>
                <desc class="x centered">304.4550749496726</desc>
                <desc class="y centered">1526.499061913696</desc>
                <desc class="x_label">PR607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="285.91573879800114"
                  y="1495.1594746716698"
                  rx="0"
                  ry="0"
                  width="32.48717934097368"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003905013193</desc>
                <desc class="x centered">302.15932846848796</desc>
                <desc class="y centered">1504.735459662289</desc>
                <desc class="x_label">p2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="309.9881993187676"
                  y="1473.3958724202628"
                  rx="0"
                  ry="0"
                  width="8.414718820207213"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00101146325</desc>
                <desc class="x centered">314.1955587288712</desc>
                <desc class="y centered">1482.971857410882</desc>
                <desc class="x_label">ss2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="257.57681506418163"
                  y="1451.6322701688555"
                  rx="0"
                  ry="0"
                  width="60.826103074793195"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.007311399136</desc>
                <desc class="x centered">287.9898666015782</desc>
                <desc class="y centered">1461.2082551594747</desc>
                <desc class="x_label">TA609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="369.4794898906411"
                  y="1429.8686679174484"
                  rx="0"
                  ry="0"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0</desc>
                <desc class="x centered">369.4794898906411</desc>
                <desc class="y centered">1439.4446529080676</desc>
                <desc class="x_label">PK610</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="309.0060596974332"
                  y="1408.1050656660414"
                  rx="0"
                  ry="0"
                  width="9.39685844154161"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001129518072</desc>
                <desc class="x centered">313.704488918204</desc>
                <desc class="y centered">1417.6810506566605</desc>
                <desc class="x_label">cs2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="311.45855085440763"
                  y="1386.341463414634"
                  rx="0"
                  ry="0"
                  width="6.944367284567193"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0008347245409</desc>
                <desc class="x centered">314.93073449669123</desc>
                <desc class="y centered">1395.9174484052533</desc>
                <desc class="x_label">SA609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="301.14643191845727"
                  y="1364.577861163227"
                  rx="0"
                  ry="0"
                  width="17.25648622051756"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.002074258453</desc>
                <desc class="x centered">309.77467502871605</desc>
                <desc class="y centered">1374.1538461538462</desc>
                <desc class="x_label">OI609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="301.3667024251629"
                  y="1342.81425891182"
                  rx="0"
                  ry="0"
                  width="17.03621571381194"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00204778157</desc>
                <desc class="x centered">309.8848102820689</desc>
                <desc class="y centered">1352.3902439024391</desc>
                <desc class="x_label">nr2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="286.5952440189441"
                  y="1321.0506566604129"
                  rx="0"
                  ry="0"
                  width="31.807674120030754"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003823335531</desc>
                <desc class="x centered">302.4990810789594</desc>
                <desc class="y centered">1330.626641651032</desc>
                <desc class="x_label">AP610</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="368.14493312798163"
                  y="1299.2870544090056"
                  rx="0"
                  ry="0"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0</desc>
                <desc class="x centered">368.14493312798163</desc>
                <desc class="y centered">1308.8630393996248</desc>
                <desc class="x_label">op2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="292.59847643019225"
                  y="1277.5234521575985"
                  rx="0"
                  ry="0"
                  width="25.804441708782576"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003101736973</desc>
                <desc class="x centered">305.50069728458357</desc>
                <desc class="y centered">1287.0994371482177</desc>
                <desc class="x_label">lg2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="295.1985334882211"
                  y="1255.7598499061912"
                  rx="0"
                  ry="0"
                  width="23.204384650753752"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.002789205774</desc>
                <desc class="x centered">306.800725813598</desc>
                <desc class="y centered">1265.3358348968104</desc>
                <desc class="x_label">ni2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="299.2394237377966"
                  y="1233.9962476547842"
                  rx="0"
                  ry="0"
                  width="19.16349440117824"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00230348402</desc>
                <desc class="x centered">308.8211709383857</desc>
                <desc class="y centered">1243.5722326454033</desc>
                <desc class="x_label">ru2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="304.39390585887367"
                  y="1212.232645403377"
                  rx="0"
                  ry="0"
                  width="14.00901228010116"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001683906663</desc>
                <desc class="x centered">311.39841199892425</desc>
                <desc class="y centered">1221.8086303939963</desc>
                <desc class="x_label">bu2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="308.5376839317989"
                  y="1190.46904315197"
                  rx="0"
                  ry="0"
                  width="9.865234207175945"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001185817621</desc>
                <desc class="x centered">313.47030103538685</desc>
                <desc class="y centered">1200.0450281425892</desc>
                <desc class="x_label">y2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="327.9517818354431"
                  y="1168.705440900563"
                  rx="0"
                  ry="0"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0</desc>
                <desc class="x centered">327.9517818354431</desc>
                <desc class="y centered">1178.2814258911822</desc>
                <desc class="x_label">T2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="275.7942010741272"
                  y="1146.941838649156"
                  rx="0"
                  ry="0"
                  width="42.60871706484761"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.005121638924</desc>
                <desc class="x centered">297.098559606551</desc>
                <desc class="y centered">1156.517823639775</desc>
                <desc class="x_label">i2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="306.6557393661543"
                  y="1125.1782363977484"
                  rx="0"
                  ry="0"
                  width="11.747178772820519"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0014120305</desc>
                <desc class="x centered">312.52932875256454</desc>
                <desc class="y centered">1134.7542213883676</desc>
                <desc class="x_label">rr2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="305.21852510108073"
                  y="1103.4146341463413"
                  rx="0"
                  ry="0"
                  width="13.184393037894097"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001584786054</desc>
                <desc class="x centered">311.8107216200278</desc>
                <desc class="y centered">1112.9906191369605</desc>
                <desc class="x_label">TL2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="316.4456998622813"
                  y="1081.6510318949342"
                  rx="0"
                  ry="0"
                  width="1.9572182766935384"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0002352609043</desc>
                <desc class="x centered">317.42430900062806</desc>
                <desc class="y centered">1091.2270168855534</desc>
                <desc class="x_label">TF2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="318.2407823005212"
                  y="1059.8874296435272"
                  rx="0"
                  ry="0"
                  width="0.16213583845365065"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-1.948899846e-05</desc>
                <desc class="x centered">318.321850219748</desc>
                <desc class="y centered">1069.4634146341464</desc>
                <desc class="x_label">TS2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="288.6757797783926"
                  y="1038.1238273921201"
                  rx="0"
                  ry="0"
                  width="29.727138360582217"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003573251659</desc>
                <desc class="x centered">303.5393489586837</desc>
                <desc class="y centered">1047.6998123827393</desc>
                <desc class="x_label">SH607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="304.8936064456423"
                  y="1016.3602251407132"
                  rx="0"
                  ry="0"
                  width="12.714646299606784"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001528321712</desc>
                <desc class="x centered">311.2509295954457</desc>
                <desc class="y centered">1025.9362101313322</desc>
                <desc class="x_label">cu2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="297.8281766165053"
                  y="994.5966228893058"
                  rx="0"
                  ry="0"
                  width="18.785633563993713"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.002258064516</desc>
                <desc class="x centered">307.2209933985022</desc>
                <desc class="y centered">1004.1726078799248</desc>
                <desc class="x_label">bc2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="298.8082128737057"
                  y="972.8330206378987"
                  rx="0"
                  ry="0"
                  width="16.795461655945076"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00201884253</desc>
                <desc class="x centered">307.2059437016783</desc>
                <desc class="y centered">982.4090056285178</desc>
                <desc class="x_label">m2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="260.12374471052317"
                  y="951.0694183864915"
                  rx="0"
                  ry="0"
                  width="55.36521475702904"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.006654991243</desc>
                <desc class="x centered">287.80635208903766</desc>
                <desc class="y centered">960.6454033771106</desc>
                <desc class="x_label">ao2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="295.00766502617546"
                  y="929.3058161350845"
                  rx="0"
                  ry="0"
                  width="18.716202490239596"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.002249718785</desc>
                <desc class="x centered">304.36576627129523</desc>
                <desc class="y centered">938.8818011257035</desc>
                <desc class="x_label">b2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="283.79045808050205"
                  y="907.5422138836773"
                  rx="0"
                  ry="0"
                  width="29.667822907262348"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003566121842</desc>
                <desc class="x centered">298.6243695341332</desc>
                <desc class="y centered">917.1181988742964</desc>
                <desc class="x_label">hc2610</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="301.0088129871286"
                  y="885.7786116322702"
                  rx="0"
                  ry="0"
                  width="12.42436082274719"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001493428913</desc>
                <desc class="x centered">307.2209933985022</desc>
                <desc class="y centered">895.3545966228893</desc>
                <desc class="x_label">pb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="291.9586968836931"
                  y="864.0150093808629"
                  rx="0"
                  ry="0"
                  width="21.155377004225045"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.002542911634</desc>
                <desc class="x centered">302.5363853858056</desc>
                <desc class="y centered">873.590994371482</desc>
                <desc class="x_label">rb2610</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="299.87085500867227"
                  y="842.251407129456"
                  rx="0"
                  ry="0"
                  width="10.810370159342938"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001299424541</desc>
                <desc class="x centered">305.27604008834373</desc>
                <desc class="y centered">851.827392120075</desc>
                <desc class="x_label">SR609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="326.8489607855858"
                  y="820.4878048780487"
                  rx="0"
                  ry="0"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0</desc>
                <desc class="x centered">326.8489607855858</desc>
                <desc class="y centered">830.0637898686678</desc>
                <desc class="x_label">bb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="279.57280375432407"
                  y="798.7242026266415"
                  rx="0"
                  ry="0"
                  width="24.26882149040688"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.002917152859</desc>
                <desc class="x centered">291.7072144995275</desc>
                <desc class="y centered">808.3001876172606</desc>
                <desc class="x_label">si2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="289.9385722366336"
                  y="776.9606003752347"
                  rx="0"
                  ry="0"
                  width="12.93833904651865"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001555209953</desc>
                <desc class="x centered">296.40774175989293</desc>
                <desc class="y centered">786.5365853658537</desc>
                <desc class="x_label">CF609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="249.06294655853566"
                  y="755.1969981238274"
                  rx="0"
                  ry="0"
                  width="41.8928994965155"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.005035596458</desc>
                <desc class="x centered">270.0093963067934</desc>
                <desc class="y centered">764.7729831144464</desc>
                <desc class="x_label">RS609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="332.7466284957187"
                  y="733.4333958724203"
                  rx="0"
                  ry="0"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">0</desc>
                <desc class="x centered">332.7466284957187</desc>
                <desc class="y centered">743.0093808630394</desc>
                <desc class="x_label">c2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="261.695226030917"
                  y="711.6697936210132"
                  rx="0"
                  ry="0"
                  width="23.350226162141325"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.002806736167</desc>
                <desc class="x centered">273.3703391119877</desc>
                <desc class="y centered">721.2457786116323</desc>
                <desc class="x_label">sp2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="279.16950422809674"
                  y="689.906191369606"
                  rx="0"
                  ry="0"
                  width="3.736515610559877"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0004491354143</desc>
                <desc class="x centered">281.0377620333767</desc>
                <desc class="y centered">699.482176360225</desc>
                <desc class="x_label">CY607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="230.1911273022601"
                  y="668.1425891181987"
                  rx="0"
                  ry="0"
                  width="47.04628844624773"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.005655042413</desc>
                <desc class="x centered">253.71427152538396</desc>
                <desc class="y centered">677.7185741088177</desc>
                <desc class="x_label">pp2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="264.4978295412764"
                  y="646.3789868667918"
                  rx="0"
                  ry="0"
                  width="12.577854006129655"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00151187905</desc>
                <desc class="x centered">270.78675654434124</desc>
                <desc class="y centered">655.9549718574109</desc>
                <desc class="x_label">ad2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="249.61802339079435"
                  y="624.6153846153845"
                  rx="0"
                  ry="0"
                  width="25.341803328276967"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003046127067</desc>
                <desc class="x centered">262.28892505493286</desc>
                <desc class="y centered">634.1913696060036</desc>
                <desc class="x_label">RM609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="255.91489047845442"
                  y="602.8517823639775"
                  rx="0"
                  ry="0"
                  width="13.510924899572046"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001624035729</desc>
                <desc class="x centered">262.67035292824045</desc>
                <desc class="y centered">612.4277673545965</desc>
                <desc class="x_label">al2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="234.65443826345611"
                  y="581.0881801125702"
                  rx="0"
                  ry="0"
                  width="34.306606214067955"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00412371134</desc>
                <desc class="x centered">251.80774137049008</desc>
                <desc class="y centered">590.6641651031892</desc>
                <desc class="x_label">PL608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="215.81229722891948"
                  y="559.3245778611633"
                  rx="0"
                  ry="0"
                  width="33.29099618935493"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00400163332</desc>
                <desc class="x centered">232.45779532359694</desc>
                <desc class="y centered">568.9005628517824</desc>
                <desc class="x_label">IF2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="240.73348940508043"
                  y="537.5609756097563"
                  rx="0"
                  ry="0"
                  width="8.052122201353342"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0009678785312</desc>
                <desc class="x centered">244.7595505057571</desc>
                <desc class="y centered">547.1369606003753</desc>
                <desc class="x_label">au2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="228.86729115876113"
                  y="515.797373358349"
                  rx="0"
                  ry="0"
                  width="18.12030546028123"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.002178090967</desc>
                <desc class="x centered">237.92744388890173</desc>
                <desc class="y centered">525.373358348968</desc>
                <desc class="x_label">l2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="152.22360214573703"
                  y="494.0337711069417"
                  rx="0"
                  ry="0"
                  width="89.69906260998647"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01078197707</desc>
                <desc class="x centered">197.07313345073027</desc>
                <desc class="y centered">503.6097560975608</desc>
                <desc class="x_label">eb2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="175.4870594143645"
                  y="472.27016885553485"
                  rx="0"
                  ry="0"
                  width="65.96116556520437"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00792864222</desc>
                <desc class="x centered">208.46764219696666</desc>
                <desc class="y centered">481.846153846154</desc>
                <desc class="x_label">sc2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="171.42952737745313"
                  y="450.50656660412756"
                  rx="0"
                  ry="0"
                  width="69.0994299848943"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.008305866842</desc>
                <desc class="x centered">205.97924236990028</desc>
                <desc class="y centered">460.0825515947467</desc>
                <desc class="x_label">bz2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="227.60173104289095"
                  y="428.74296435272026"
                  rx="0"
                  ry="0"
                  width="4.908172275463983"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.0005899705015</desc>
                <desc class="x centered">230.05581718062294</desc>
                <desc class="y centered">438.3189493433394</desc>
                <desc class="x_label">wr2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="182.5201035211404"
                  y="406.9793621013132"
                  rx="0"
                  ry="0"
                  width="48.87871029418514"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.005875302578</desc>
                <desc class="x centered">206.95945866823297</desc>
                <desc class="y centered">416.55534709193233</desc>
                <desc class="x_label">sn2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="206.3967861981982"
                  y="385.21575984990614"
                  rx="0"
                  ry="0"
                  width="23.173682470505554"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00278551532</desc>
                <desc class="x centered">217.98362743345098</desc>
                <desc class="y centered">394.79174484052527</desc>
                <desc class="x_label">lh2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="195.67275154597107"
                  y="363.45215759849907"
                  rx="0"
                  ry="0"
                  width="30.682541648250947"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003688092729</desc>
                <desc class="x centered">211.01402237009654</desc>
                <desc class="y centered">373.0281425891182</desc>
                <desc class="x_label">UR609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="179.58858750936585"
                  y="341.688555347092"
                  rx="0"
                  ry="0"
                  width="43.736021979191804"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.005257142857</desc>
                <desc class="x centered">201.45659849896174</desc>
                <desc class="y centered">351.26454033771114</desc>
                <desc class="x_label">lc2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="188.95758469810195"
                  y="319.9249530956847"
                  rx="0"
                  ry="0"
                  width="11.616888898539855"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.001396369439</desc>
                <desc class="x centered">194.76602914737188</desc>
                <desc class="y centered">329.50093808630385</desc>
                <desc class="x_label">zn2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="163.4202621226972"
                  y="298.1613508442779"
                  rx="0"
                  ry="0"
                  width="35.09041268293066"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.004217926186</desc>
                <desc class="x centered">180.96546846416254</desc>
                <desc class="y centered">307.737335834897</desc>
                <desc class="x_label">MA609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="144.0267277161234"
                  y="276.3977485928706"
                  rx="0"
                  ry="0"
                  width="54.41526509649225"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.006540805708</desc>
                <desc class="x centered">171.2343602643695</desc>
                <desc class="y centered">285.9737335834897</desc>
                <desc class="x_label">pd2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="153.98662128495428"
                  y="254.6341463414633"
                  rx="0"
                  ry="0"
                  width="39.97793519395782"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.004805414552</desc>
                <desc class="x centered">173.9755888819332</desc>
                <desc class="y centered">264.2101313320824</desc>
                <desc class="x_label">IH2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="154.88462007209424"
                  y="232.87054409005648"
                  rx="0"
                  ry="0"
                  width="37.29364692753424"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.004482758621</desc>
                <desc class="x centered">173.53144353586134</desc>
                <desc class="y centered">242.44652908067562</desc>
                <desc class="x_label">br2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="126.89749185568085"
                  y="211.1069418386492"
                  rx="0"
                  ry="0"
                  width="51.216567494369386"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.006156316916</desc>
                <desc class="x centered">152.50577560286555</desc>
                <desc class="y centered">220.68292682926833</desc>
                <desc class="x_label">ps2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="123.76567198797045"
                  y="189.3433395872419"
                  rx="0"
                  ry="0"
                  width="51.90326564026773"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.00623885918</desc>
                <desc class="x centered">149.7173048081043</desc>
                <desc class="y centered">198.91932457786103</desc>
                <desc class="x_label">eg2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="130.1831634180502"
                  y="167.57973733583484"
                  rx="0"
                  ry="0"
                  width="42.34458878138324"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.005089890264</desc>
                <desc class="x centered">151.35545780874185</desc>
                <desc class="y centered">177.15572232645397</desc>
                <desc class="x_label">IC2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="38.892134935145535"
                  y="145.81613508442777"
                  rx="0"
                  ry="0"
                  width="119.79033565878383"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01439899833</desc>
                <desc class="x centered">98.78730276453746</desc>
                <desc class="y centered">155.3921200750469</desc>
                <desc class="x_label">lu2607</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="101.07397333982387"
                  y="124.05253283302069"
                  rx="0"
                  ry="0"
                  width="51.386221614733174"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.006176709625</desc>
                <desc class="x centered">126.76708414719045</desc>
                <desc class="y centered">133.62851782363984</desc>
                <desc class="x_label">IM2606</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="99.96632388533907"
                  y="102.28893058161363"
                  rx="0"
                  ry="0"
                  width="51.81726980249847"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.006228522337</desc>
                <desc class="x centered">125.87495878658831</desc>
                <desc class="y centered">111.86491557223277</desc>
                <desc class="x_label">ag2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="95.52486334278868"
                  y="80.52532833020634"
                  rx="0"
                  ry="0"
                  width="32.14587328791143"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.003863987635</desc>
                <desc class="x centered">111.59779998674439</desc>
                <desc class="y centered">90.10131332082548</desc>
                <desc class="x_label">fu2609</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="34.48919888808643"
                  y="58.7617260787995"
                  rx="0"
                  ry="0"
                  width="85.00410756014594"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.01021763564</desc>
                <desc class="x centered">76.9912526681594</desc>
                <desc class="y centered">68.33771106941865</desc>
                <desc class="x_label">pt2608</desc>
              </g>
              <g
                class="bar"
                style="fill: none; stroke: #22c55e; stroke-width: 3"
              >
                <rect
                  x="11.253846153846146"
                  y="36.998123827392206"
                  rx="0"
                  ry="0"
                  width="52.65412662602202"
                  height="19.151969981238278"
                  class="rect reactive tooltip-trigger"
                />
                <desc class="value">-0.006329113924</desc>
                <desc class="x centered">37.58090946685716</desc>
                <desc class="y centered">46.57410881801135</desc>
                <desc class="x_label">pg2607</desc>
              </g>
            </g>
          </g>
        </g>
        <g class="titles">
          <text x="350.0" y="40" class="title plot_title">
            国内商品(2026-05-27)
          </text>
        </g>
        <g transform="translate(94, 60)" class="plot overlay">
          <g class="series serie-0 color-0" />
          <g class="series serie-1 color-1" />
          <g class="series serie-2 color-2" />
        </g>
        <g transform="translate(94, 60)" class="plot text-overlay">
          <g class="series serie-0 color-0" />
          <g class="series serie-1 color-1" />
          <g class="series serie-2 color-2" />
        </g>
        <g transform="translate(94, 60)" class="plot tooltip-overlay">
          <g transform="translate(0 0)" style="opacity: 0" class="tooltip">
            <rect rx="0" ry="0" width="0" height="0" class="tooltip-box" />
            <g class="text" />
          </g>
        </g>
      </g>
    </svg>"""  # 你的 Pygal 输出
inline_svg = svg_css_to_inline(svg_code)
# print(inline_svg)
with open("bar.html", "w", encoding="utf-8") as f:
    f.write(inline_svg)
