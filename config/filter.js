function filter(node) {
    if(node.Remark.includes('伊拉克'))
        return false;
    return true;
}

// const node = 
// {
//     "Remark": "伊拉克 01 �| ws",
// }

// console.log(filter(node))