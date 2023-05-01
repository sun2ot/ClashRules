function filter(node) {
    if(node.Remark.includes(`\_`))
        return false;
    return true;
}

// const node = 
// {
//     "Remark": "伊拉克 01 \_| ws",
// }

// console.log(filter(node))