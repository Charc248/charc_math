class SemiGroupElement(object):
    def operation(self, other):
        pass
    
class GroupElement(SemiGroupElement):
    def inverse(self):
        pass
    
    @classmethod
    def identity(cls):
        pass
    
class AbelianGroupElement(GroupElement):
    def add(self, other):
        return self.operation(other)
        
class SemiRingElement(object):
    def add(self, other):
        pass
    
    @classmethod
    def additive_identity(cls):
        pass
    
    def multiply(self, other):
        pass
    
    @classmethod
    def multiplicative_identity(cls):
        pass
    
class RingElement(SemiRingElement):
    def additive_inverse(self):
        pass
    
class FieldElement(RingElement):
    def multiplicative_inverse(self):
        pass