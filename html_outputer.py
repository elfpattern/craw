#coding:utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []  #数据容器

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)    #收集数据

    def output_html(self):                    #输出数据
        fout = open('output.html','w', encoding='utf-8')

        fout.write('<html>')     #表示一个html身体
        fout.write('<body>')     #写一个body
        fout.write('<table>')    #把数据输出成表格的形式

        for data in self.datas:
            fout.write('<tr>')    #写一个行的开始标签
            fout.write('<td>%s</td>' % data['url'])  #输出每个单元格的内容
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()