class TextBorder:
    def __init__(self):
        pass


    def single_border(self, text):
        lines = text.split('\n')
        width = max(len(s) for s in lines)
        border = '+' + '-' * (width + 2) + '+'
        sides = '|'
        result = [border]
        for line in lines:
            result.append(f'{sides} {line.ljust(width)} {sides}')
        result.append(border)
        return '\n'.join(result)


    def double_border(self, text):
        lines = text.split('\n')
        width = max(len(s) for s in lines)
        border = '+' + '=' * (width + 4) + '+'
        sides = '||'
        result = [border]
        for line in lines:
            result.append(f'{sides} {line.ljust(width)} {sides}')
        result.append(border)
        return '\n'.join(result)


    def dashed_border(self, text):
        lines = text.split('\n')
        width = max(len(s) for s in lines)
        border = '+' + '_' * (width + 2) + '+'
        sides = '|'
        lines[0] = lines[0].replace('-', '=')
        lines[-1] = lines[-1].replace('-', '=')
        result = [border]
        for line in lines:
            result.append(f'{sides} {line.ljust(width)} {sides}')
        result.append(border)
        return '\n'.join(result)
