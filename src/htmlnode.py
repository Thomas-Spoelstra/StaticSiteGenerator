class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
       self.tag = tag
       self.value = value
       self.children = children
       self.props = props 

    def __repr__(self):
        return(f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}")
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self): 

        if self.props == None:
            return ""
        
        items = self.props.items()
        result = f""
        quote = "\""
        
        for key, value in items:
            result += " " + key + "=" + quote + value + quote
        return result
        
        