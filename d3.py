# basics-python-3

✅ Variables and references
     a = [1, 2]
      b = a
    b.append(3)
    print(a)  # [1,2,3]
  {=} creates another label for the same obj

✅ Mutable vs immutable objects
  Immutable (int, str, tuple)
  Mutable (list, dict, set)
    Immutable → creates new object.
    Mutable → modifies existing object.
      
✅ Function parameter passing
    Functions receive references to objects, not copies.
        def add(lst):
          lst.append(3)

        a = [1, 2]
        add(a)

    print(a)  # [1,2,3]

✅ Local variable lifetime
     It dies when the function ends

✅ The mutable default argument trap
    Default mutable objects are created once, not on every call.
      def add(x, lst=[]):
          lst.append(x)
          return lst

      print(add(1))  # [1]
      print(add(2))  # [1,2]
