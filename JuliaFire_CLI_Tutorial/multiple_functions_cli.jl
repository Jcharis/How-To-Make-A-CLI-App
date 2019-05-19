using Fire

" A simple Greet Function"
@main function greet(name)
    println("Hello ",name)
end

" Add Multiple Numbers"
@main function add(num::Integer...)
    println("Adding Numbers :",num)
    println(sum(num))
end

" Reverse A String"
@main function reversestring(text::AbstractString)
    println(text[end:-1:1])
end

