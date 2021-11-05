var numbers = [5,2,6,3,0,1,9,8];
console.log(sortNumbers(numbers));
function sortNumbers(numbers){
    var i = 1;
    var temp;
    var count;
    while(i){
        count = 0;
        for(var index=0; index<numbers.length-1; index++){
            if(numbers[index] < numbers[index+1]){ // decreasing order sorting
                temp = numbers[index+1];
                numbers[index+1] = numbers[index];
                numbers[index] = temp;
            }
            else{
                count++; // more count -> more sorted array
            }
        }
        if(count == numbers.length-1){
            i = 0; // stop the while loop
        }
    }
    return numbers;
}