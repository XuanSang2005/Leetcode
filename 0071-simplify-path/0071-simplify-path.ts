function simplifyPath(path: string): string {
    const components: string[] = path.split('/');
    const stack: string[] = [];
    components.forEach((part) =>{
        if (part === ".."){
            if (stack.length > 0 ){
                stack.pop();
            }
        }
        else if (part !== "" && part !== "." ){
            stack.push(part);
        }
    });
    return "/" + stack.join("/");
};