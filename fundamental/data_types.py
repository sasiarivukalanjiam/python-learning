import cmath

class data_types(object):

    def none_type(self):
        """
        
        :return: 
        """
        a = None
        print(a)

    def numertic_type(self):
        """
        
        :return: 
        """
        int_ex = 57
        float1_ex = 57.66666
        float2_ex = 55.66e6
        print(int_ex, float1_ex, float2_ex)
        complex_ex1 = complex(1,3)
        complex_ex2 = complex(2,4)
        complex_add = complex_ex1 + complex_ex2
        print(complex_ex1.real, complex_ex1.imag)
        sin_value = cmath.sin(complex_add)
        print(sin_value)
        binaryb = 0b1010101
        binaryB = 0B0101010
        octalo = 0o754
        octalO = 0O754
        hexx = 0x45612
        hexX = 0X45612
        print(sin_value, binaryb, binaryB, octalo, octalO, hexx, hexX)
        x = 5.55
        conv_int_x = int(x)
        float_it = float(conv_int_x)
        to_complex = complex(conv_int_x)
        sample = "2d3"
        base_conv16 = int(sample, 16)
        print(float_it, to_complex, base_conv16)
        value = 17
        bin_value = bin(value)
        oct_value = oct(value)
        hex_value = hex(value)
        print("bin , oct , hex {0} {1} {2}".format(bin_value, oct_value, hex_value))
        # boolean example
        b = 10 < 15
        print(type(b))
        print(b)

    def sequence_type(self):
        pass

    def set_type(self):
        pass

    def mapping_type(self):
        pass

if __name__ == '__main__':
    d = data_types()
    d.none_type()
    d.numertic_type()
    d.sequence_type()
    d.set_type()
    d.mapping_type()