import re

is_part = r'第.部分'
is_chapter = r'第.{1,2}章'
is_appendix = r'附录.'
page_bias = 26
page_bias_on = False

with open('input.txt', 'r', encoding='utf-8') as inputf:
    with open('output.txt', 'w', encoding='utf-8') as outputf:
        level = 0
        for line in inputf.readlines():
            # preprocess
            line = line.strip()
            components = line.split(' ')
            while len(components) > 3:
                components[1] = components[1]+components[2]
                components.remove(components[2])
            # determine the type
            dotcount = components[0].count('.')
            if dotcount > 0:
                level = dotcount
                content = components[0]+' '+components[1]
                page = int(components[2])
            elif re.match(is_part, components[0]):
                level = 0
                content = components[0]+' '+components[1]
                page = int(components[2])
            elif re.match(is_chapter, components[0]):
                level = 0
                content = components[0]+' '+components[1]
                page = int(components[2])
            elif re.match(is_appendix, components[0]):
                level = 0
                content = components[0]+' '+components[1]
                page = int(components[2])
            elif components[0] == '---':
                page_bias_on = True
                continue
            else:
                content = components[0]
                page = int(components[1])
            # bias
            if page_bias_on:
                page += page_bias
            # output
            outputf.write('\t'*level+content+'\t'+str(page)+'\n')
