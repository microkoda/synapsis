def format_to_limit(text: str, max_width: int) -> list:
    """
    Function splits text to the lines width specified max_width of length.
    
    Parameters:
        text(str): text to be formatted

    Returns:
        formated_text(list):list of lines.
   
    Example:
    
    >>> format_to_limit("Hey there mate, it’s nice to finally meet you!", 16)
    ['Hey there mate,', 'it’s nice to', 'finally meet', 'you!']
    
    """
    class Itertext:
        def __init__(self, text):
            self.text = text
            self.lenght = len(self.text)
            self.i = 0

        def __len__(self):
            return self.lenght

        def next_(self):
            if self.i >= self.lenght:
                raise StopIteration
            else:
                word = self.text[self.i]
                self.i +=1
                return word

    it = Itertext(text.split())
    summary_line_length = 0
    formated_text = []
    line = []
    word = it.next_()
    i = 1
    summary_line_length += len(word)
    line.append(word)
    while True:
        try:
            word = it.next_()
            while summary_line_length + len(word) + i < max_width:
                line.append(word)
                i += 1
                summary_line_length += len(word)
                word = it.next_()
            formated_text.append(' '.join(line))
            line = []     
            line.append(word)
            i = 1
            summary_line_length = len(word)
        except StopIteration:
            formated_text.append(' '.join(line))
            break
    return formated_text

if __name__ == "__main__":
    import doctest
    doctest.testmod()