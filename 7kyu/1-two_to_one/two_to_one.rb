def longest(a1, a2)
 p a1.chars.uniq.join
 p a2.chars.uniq.join
end

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"
